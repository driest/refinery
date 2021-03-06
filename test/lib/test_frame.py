#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import refinery as r

from refinery.lib.frame import FrameUnpacker
from refinery.units import LogLevel

from .. import TestBase


class TestFraming(TestBase):

    def test_simple_frame(self):
        chunks = [B'A' * k for k in (0x14, 0x154, 0x81, 0x12031, 0x1311, 0x8012)]
        buffer = io.BytesIO()
        for chunk in (io.BytesIO(B'\n'.join(chunks)) | r.resplit('[')):
            buffer.write(chunk)
        buffer.seek(0)
        expected = []
        unpacked = FrameUnpacker(buffer)
        while unpacked.nextframe():
            expected.extend(c for c in unpacked)
        self.assertEqual(chunks, expected)

    def test_layered_frame_01(self):
        p = r.chop(4, '[') | r.chop(2, '[') | r.ccp('F', ']') | r.cca('?') | r.sep(']')
        self.assertEqual(p(B'OOOO' * 12), B'\n'.join([B'FOOFOO?'] * 12))

    def test_layered_frame_02(self):
        p = r.chop(4) [ r.chop(2) [ r.emit('F', 'x::') ]| r.emit('x::', '?') [r.nop] | r.sep ] # noqa
        self.assertEqual(p(B'OOOO' * 12), B'\n'.join([B'FOOFOO?'] * 12))

    def test_documentation_example_01(self):
        self.assertEqual(B'FOO.FOO.FOO.FOO.', (r.chop(2)[r.ccp('F') | r.cca('.')])(B'OOOOOOOO'))

    def test_documentation_example_02(self):
        self.assertEqual(B'FOO.FOO.\nFOO.FOO.', (r.chop(4)[r.chop(2)[r.ccp('F') | r.cca('.')] | r.sep])(B'OOOOOOOO'))

    def test_documentation_example_03(self):
        self.assertEqual(B'binary-REFINERY',
            (r.emit('BINARY', 'REFINERY')[r.scope(0) | r.clower | r.sep('-')])(B'')
        )

    def test_documentation_example_04(self):
        self.assertEqual(B'NaNaNaNaNaNaNaNa-Batman',
            (r.emit('aaaaaaaa', 'namtaB')[r.scope(0) | r.rex('.')[r.ccp('N')] | r.scope(1) | r.rev | r.sep('-')])(B'')
        )

    def test_real_world_01(self):
        encoded = B'''301815214850156721331018480063340936214488055910529404970112631124608113197561534315323106291311611118111571030916590053421252410301171850583912575068111856414554157930507606789054031912510227182600807906431133491248306004123002146510940169690710820141169320955312014120171102115059068660995810412198261688106236171480925510919175470806111215112451580216678065680593716920140350943309471097820618705622181381760512207200740695112292051860572813684059730540612867133770664415988405914129061377506879064041396607792051271161313019124720712811569074680757406931112780654609788055291148605702141810628505815128490945608789054940492611748095590847706617126221215309060083411027606705138001434509852091211222411908135111322312025118181250314030113440993311087056570868006343100341090114209134640795408939104470969005365078580853510871072121313211155088071361612710133620813710651092820619305073070401034210170073610823810550093830603610763080201236707691052400143051380813527116720712411948095460972511826117830604909480063550881313020123700732911434109111327107252091820612112243100171263111266077191245908460083860575009354089740698805569074161279005364079321115309035108401031812509134770666308092051560874210137106680758405975068670761013351092730709105236107381053311058085141294409981062930500713676067850583910402141121311512865078790647806541102620815708606137890546108294049031402811547096011424509822121301130413987056231204'''
        decoded = B'''wMIc  'prOcess'   "cALl"  crEAtE   "powErsHell  -NoNiNtErAC -NoPrOFi -WIn 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'''
        pl = r.chop(476) [ r.chop(5, '-t') [ r.sorted | r.snip('2:') | r.sep ]| r.pack(10) | r.blockop('--dec', '-sN', 'B-S') ] # noqa
        self.assertEqual(decoded, pl(encoded))

    def test_nonblocking(self):
        with io.BytesIO(bytes(range(20))) as stream:
            slow = stream | r.rex('.')
            for k in range(20):
                self.assertEqual(slow.read1(20), bytes((k,)))

    def test_nonblocking_frame_collapse(self):
        with io.BytesIO(bytes(range(20))) as stream:
            slow = stream | r.chop(5) [ r.rex('.') ] # noqa
            for k in range(20):
                self.assertEqual(slow.read1(20), bytes((k,)))

    def test_depth3(self):
        pl = r.snip(':3', 3, 4, '5:')[r.scope('1:3') | r.rex('.')[r.rep(3)[r.ccp('X')]]]
        self.assertEqual(B'AAAXBXBXBXCXCXCDDD', pl(B'AAABCDDD'))

    def test_continue_after_error(self):
        T = self.generate_random_buffer(16)
        aes = r.aes('CBC', key=T, iv=T)
        msg = [self.generate_random_buffer(3*16) for _ in range(12)]
        hidden = msg[7]
        msg[7] = aes.reverse(hidden)
        pipeline = r.emit(data=msg)[aes]
        pipeline.log_level = LogLevel.NONE
        self.assertEqual(aes(msg[7]), hidden)
        self.assertEqual(pipeline(B''), hidden)