#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from . import TestUnitBase

from refinery.lib import loader
from refinery import neg, b64, repl, rex, pack, sub


class TestPipelines(TestUnitBase):

    def test_link_loader_tb01(self):
        pipeline = repl('Grk', ')+chr(') | rex(R'chr.(\d+)-(\d+).', '$1,$2,') | pack() | sub('x:1::2')
        payload = B'chr(118-7Grk119-9Grk38-6Grk104-3Grk116-2Grk119-5Grk117-6Grk120-6Grk36-4Grk116-2Grk110-9Grk119-4Grk124-7Grk110-1Grk102-1Grk39-7Grk111-1Grk103-2Grk124-4Grk125-9Grk14-1Grk19-9Grk123-8Grk103-2Grk123-7Grk36-4Grk89-2Grk119-4Grk113-9Grk90-7Grk106-2Grk102-1Grk116-8Grk115-7Grk37-5Grk67-6Grk39-7Grk73-6Grk117-3Grk110-9Grk104-7Grk123-7Grk110-9Grk80-1Grk106-8Grk112-6Grk106-5Grk105-6Grk120-4Grk41-1Grk38-4Grk93-6Grk90-7Grk102-3Grk117-3Grk106-1Grk118-6Grk125-9Grk48-2Grk91-8Grk112-8Grk106-5Grk117-9Grk113-5Grk40-6Grk49-8Grk21-8Grk16-6Grk87-4Grk106-5Grk119-3Grk38-6Grk76-6Grk90-7Grk83-4Grk37-5Grk68-7Grk35-3Grk75-8Grk115-1Grk105-4Grk99-2Grk125-9Grk106-5Grk87-8Grk102-4Grk110-4Grk102-1Grk104-5Grk121-5Grk43-3Grk36-2Grk86-3Grk101-2Grk120-6Grk113-8Grk113-1Grk117-1Grk106-1Grk115-5Grk111-8Grk49-3Grk75-5Grk106-1Grk109-1Grk105-4Grk89-6Grk130-9Grk122-7Grk121-5Grk110-9Grk116-7Grk81-2Grk101-3Grk111-5Grk109-8Grk108-9Grk123-7Grk35-1Grk48-7Grk18-5Grk11-1Grk87-7Grk103-6Grk122-6Grk105-1Grk40-8Grk68-7Grk35-3Grk91-4Grk118-3Grk107-3Grk88-5Grk110-6Grk107-6Grk110-2Grk110-2Grk49-3Grk77-8Grk126-6Grk118-6Grk104-7Grk115-5Grk102-2Grk75-6Grk114-4Grk121-3Grk112-7Grk120-6Grk119-8Grk119-9Grk117-8Grk108-7Grk114-4Grk124-8Grk86-3Grk122-6Grk120-6Grk109-4Grk116-6Grk106-3Grk121-6Grk48-8Grk37-3Grk46-9Grk91-7Grk72-3Grk81-4Grk89-9Grk43-6Grk38-4Grk47-6Grk39-7Grk40-2Grk35-3Grk35-1Grk100-8Grk82-5Grk111-6Grk103-4Grk118-4Grk119-8Grk124-9Grk119-8Grk103-1Grk122-6Grk55-9Grk120-3Grk120-6Grk110-2Grk35-1Grk18-5Grk11-1Grk122-7Grk103-2Grk122-6Grk40-8Grk112-1Grk90-5Grk119-5Grk112-4Grk78-2Grk111-6Grk111-1Grk114-7Grk36-4Grk62-1Grk34-2Grk96-9Grk119-4Grk110-6Grk92-9Grk110-6Grk105-4Grk116-8Grk115-7Grk51-5Grk71-4Grk116-2Grk109-8Grk99-2Grk118-2Grk108-7Grk90-7Grk110-6Grk117-6Grk118-4Grk120-4Grk104-5Grk119-2Grk125-9Grk42-2Grk85-5Grk104-7Grk122-6Grk105-1Grk42-1Grk20-7Grk17-7Grk112-1Grk93-8Grk115-1Grk116-8Grk81-5Grk106-1Grk118-8Grk111-4Grk54-8Grk87-3Grk105-8Grk115-1Grk105-2Grk110-9Grk125-9Grk81-1Grk99-2Grk118-2Grk107-3Grk39-7Grk68-7Grk38-6Grk37-3Grk109-5Grk125-9Grk120-4Grk117-5Grk66-8Grk56-9Grk51-4Grk125-6Grk128-9Grk123-4Grk52-6Grk112-3Grk108-3Grk101-2Grk116-2Grk117-6Grk118-3Grk120-9Grk105-3Grk123-7Grk52-6Grk103-4Grk114-3Grk110-1Grk43-9Grk17-4Grk15-5Grk115-4Grk91-6Grk123-9Grk114-6Grk85-9Grk112-7Grk115-5Grk116-9Grk47-1Grk88-5Grk104-7Grk119-1Grk106-5Grk46-6Grk123-8Grk107-3Grk106-1Grk120-4Grk44-3Grk18-5Grk19-9Grk109-4Grk109-7Grk38-6Grk33-1Grk44-4Grk75-5Grk92-9Grk87-8Grk55-9Grk79-9Grk112-7Grk109-1Grk104-3Grk70-1Grk121-1Grk110-5Grk121-6Grk122-6Grk119-4Grk45-5Grk88-8Grk103-6Grk122-6Grk111-7Grk45-4Grk42-1Grk40-8Grk35-3Grk88-4Grk113-9Grk106-5Grk115-5Grk37-5Grk21-8Grk12-2Grk93-6Grk87-4Grk107-8Grk117-3Grk111-6Grk114-2Grk123-7Grk55-9Grk70-1Grk100-1Grk106-2Grk115-4Grk35-3Grk43-9Grk93-8Grk117-7Grk114-7Grk112-2Grk118-7Grk127-8Grk117-7Grk33-1Grk76-7Grk119-5Grk123-9Grk117-6Grk116-2Grk40-7Grk38-4Grk16-3Grk18-8Grk103-2Grk112-4Grk117-2Grk107-6Grk21-8Grk19-9Grk70-2Grk107-2Grk111-2Grk37-5Grk121-1Grk115-6Grk112-4Grk51-7Grk122-3Grk124-9Grk52-8Grk106-6Grk105-7Grk47-3Grk111-9Grk114-9Grk113-5Grk106-5Grk113-1Grk104-7Grk120-4Grk107-3Grk51-7Grk88-3Grk89-7Grk81-5Grk18-5Grk13-3Grk127-7Grk116-7Grk110-2Grk33-1Grk68-7Grk34-2Grk38-4Grk78-1Grk90-7Grk92-4Grk81-4Grk80-4Grk56-6Grk50-4Grk91-8Grk110-9Grk123-9Grk122-4Grk108-7Grk121-7Grk93-5Grk86-9Grk82-6Grk80-8Grk92-8Grk88-4Grk82-2Grk51-5Grk55-4Grk51-5Grk50-2Grk36-2Grk19-6Grk16-6Grk128-9Grk120-5Grk39-7Grk62-1Grk38-6Grk41-7Grk91-4Grk91-8Grk108-9Grk119-5Grk112-7Grk121-9Grk124-8Grk54-8Grk92-9Grk106-2Grk106-5Grk113-5Grk115-7Grk42-8Grk16-3Grk18-8Grk103-3Grk104-6Grk35-3Grk65-4Grk35-3Grk38-4Grk69-4Grk101-1Grk119-8Grk102-2Grk103-5Grk53-7Grk91-8Grk124-8Grk123-9Grk105-4Grk98-1Grk117-8Grk40-6Grk18-5Grk13-3Grk87-4Grk108-7Grk118-2Grk34-2Grk127-8Grk124-9Grk110-6Grk124-9Grk40-8Grk62-1Grk41-9Grk101-2Grk115-1Grk109-8Grk101-4Grk125-9Grk109-8Grk112-1Grk105-7Grk115-9Grk108-7Grk103-4Grk125-9Grk49-9Grk127-8Grk119-4Grk42-1Grk16-3Grk18-8Grk111-9Grk114-9Grk109-1Grk103-2Grk118-6Grk104-7Grk123-7Grk110-6Grk37-5Grk66-5Grk34-2Grk123-4Grk124-9Grk112-8Grk121-6Grk47-1Grk73-4Grk129-9Grk116-4Grk103-6Grk112-2Grk102-2Grk70-1Grk114-4Grk121-3Grk112-7Grk122-8Grk120-9Grk119-9Grk115-6Grk104-3Grk118-8Grk121-5Grk92-9Grk125-9Grk123-9Grk111-6Grk114-4Grk112-9Grk120-5Grk47-7Grk41-7Grk46-9Grk88-4Grk78-9Grk83-6Grk88-8Grk43-6Grk37-3Grk46-5Grk34-2Grk41-3Grk41-9Grk36-2Grk97-5Grk55-4Grk59-5Grk57-3Grk57-3Grk62-8Grk56-7Grk61-7Grk98-3Grk61-9Grk59-7Grk58-3Grk61-7Grk59-6Grk54-6Grk60-3Grk97-2Grk65-8Grk53-3Grk54-5Grk58-1Grk53-5Grk57-2Grk50-1Grk50-4Grk110-9Grk122-2Grk104-3Grk37-3Grk17-4Grk12-2Grk92-7Grk87-5Grk83-7Grk40-8Grk64-3Grk41-9Grk43-9Grk110-6Grk122-6Grk121-5Grk117-5Grk60-2Grk56-9Grk48-1Grk54-5Grk63-6Grk54-1Grk52-6Grk55-6Grk54-4Grk54-3Grk50-4Grk52-2Grk58-6Grk51-1Grk49-3Grk51-2Grk60-5Grk61-8Grk50-3Grk122-8Grk112-1Grk124-8Grk121-5Grk53-7Grk118-6Grk105-1Grk118-6Grk36-2Grk21-8Grk11-1Grk105-4Grk115-5Grk104-4Grk39-7Grk112-7Grk108-6Grk21-8Grk18-8Grk19-6Grk19-9Grk76-9Grk102-5Grk116-8Grk110-2Grk35-3Grk118-6Grk123-9Grk116-5Grk112-9Grk19-6Grk12-2Grk34-2Grk120-5Grk119-2Grk104-6Grk36-4Grk116-4Grk122-8Grk114-3Grk112-9Grk16-3Grk19-9Grk33-1Grk34-2Grk40-8Grk40-8Grk107-7Grk108-3Grk111-2Grk36-4Grk113-4Grk118-3Grk122-2Grk114-5Grk116-8Grk61-3Grk35-3Grk89-6Grk106-5Grk125-9Grk41-9Grk117-8Grk121-6Grk129-9Grk116-7Grk116-8Grk34-2Grk70-9Grk40-8Grk101-2Grk119-5Grk103-2Grk106-9Grk118-2Grk110-9Grk117-6Grk101-3Grk112-6Grk107-6Grk103-4Grk122-6Grk46-6Grk123-3Grk114-5Grk116-8Grk49-8Grk18-5Grk19-9Grk37-5Grk40-8Grk37-5Grk41-9Grk101-1Grk107-2Grk113-4Grk41-9Grk120-5Grk123-7Grk119-5Grk107-6Grk100-3Grk114-5Grk61-3Grk35-3Grk84-1Grk108-7Grk119-3Grk33-1Grk124-9Grk122-6Grk116-2Grk106-5Grk101-4Grk114-5Grk38-6Grk69-8Grk36-4Grk106-7Grk119-5Grk110-9Grk99-2Grk120-4Grk110-9Grk115-4Grk105-7Grk113-7Grk105-4Grk107-8Grk118-2Grk46-6Grk108-8Grk103-5Grk45-4Grk15-2Grk12-2Grk41-9Grk37-5Grk36-4Grk35-3Grk115-6Grk120-5Grk123-3Grk113-4Grk111-3Grk49-3Grk88-9Grk117-5Grk105-4Grk113-3Grk39-7Grk39-5Grk79-8Grk70-1Grk93-9Grk38-4Grk49-5Grk38-6Grk87-2Grk84-2Grk78-2Grk49-5Grk37-5Grk74-4Grk104-7Grk115-7Grk121-6Grk102-1Grk14-1Grk13-3Grk12-3Grk112-3Grk119-4Grk125-5Grk117-8Grk116-8Grk49-3Grk88-5Grk109-8Grk114-4Grk105-5Grk14-1Grk12-2Grk36-4Grk36-4Grk37-5Grk38-6Grk127-8Grk110-5Grk118-2Grk111-7Grk39-7Grk122-7Grk122-6Grk117-3Grk107-6Grk101-4Grk116-7Grk15-2Grk16-6Grk33-1Grk37-5Grk33-1Grk38-6Grk38-6Grk37-5Grk53-7Grk120-4Grk125-4Grk113-1Grk102-1Grk37-5Grk63-2Grk36-4Grk53-4Grk22-9Grk13-3Grk35-3Grk35-3Grk39-7Grk38-6Grk41-9Grk41-9Grk53-7Grk120-9Grk117-5Grk110-9Grk116-6Grk21-8Grk19-9Grk35-3Grk40-8Grk38-6Grk34-2Grk39-7Grk37-5Grk51-5Grk128-9Grk119-5Grk113-8Grk118-2Grk109-8Grk37-5Grk110-1Grk121-6Grk126-6Grk110-1Grk109-1Grk55-9Grk120-6Grk108-7Grk118-3Grk119-7Grk115-4Grk111-1Grk116-1Grk108-7Grk69-3Grk113-2Grk108-8Grk122-1Grk22-9Grk14-4Grk36-4Grk37-5Grk35-3Grk34-2Grk34-2Grk33-1Grk50-4Grk120-5Grk106-9Grk120-2Grk102-1Grk117-1Grk115-4Grk110-8Grk110-5Grk111-3Grk104-3Grk35-3Grk106-4Grk114-9Grk116-8Grk104-3Grk115-3Grk103-6Grk120-4Grk110-6Grk53-9Grk34-2Grk54-4Grk15-2Grk12-2Grk17-8Grk102-1Grk112-2Grk101-1Grk36-4Grk128-9Grk110-5Grk121-5Grk113-9Grk17-4Grk11-1Grk39-7Grk126-7Grk123-8Grk107-3Grk118-3Grk52-6Grk74-5Grk129-9Grk108-7Grk107-8Grk47-7Grk105-3Grk113-8Grk109-1Grk106-5Grk116-4Grk102-5Grk121-5Grk111-7Grk47-6Grk16-3Grk12-2Grk38-6Grk106-5Grk112-2Grk102-2Grk33-1Grk116-1Grk122-5Grk104-6Grk15-2Grk16-6Grk77-7Grk87-4Grk85-6Grk54-8Grk79-8Grk105-4Grk121-5Grk74-4Grk111-6Grk112-4Grk102-1Grk48-8Grk95-8Grk89-6Grk102-3Grk119-5Grk106-1Grk116-4Grk117-1Grk49-3Grk90-7Grk105-6Grk122-8Grk106-1Grk113-1Grk121-5Grk79-9Grk125-8Grk111-3Grk113-5Grk86-8Grk102-5Grk112-3Grk110-9Grk50-9Grk54-8Grk104-4Grk103-2Grk110-2Grk105-4Grk117-1Grk104-3)'
        decoded = pipeline(payload).decode(pipeline.codec)
        self.assertTrue('195.123.242.175' in decoded)


class TestMetaProperties(TestUnitBase):

    def test_unique_entry_point_names(self):
        entry_points = set()
        for entry in loader.get_all_entry_points():
            self.assertNotIn(entry.__qualname__, entry_points)
            entry_points.add(entry.__qualname__)
        self.assertGreaterEqual(len(entry_points), 10)


class TestSimpleInvertible(TestUnitBase):
    exceptions = ['vbe', 'u16', 'cp1252']

    def setUp(self):
        super().setUp()
        self.invertibles = {}
        self.structured_buffers = [
            B'A' * 1024,
            B'B' + B'A' * 1024,
            B'FOO' * 200,
            bytes(range(1, 200))
        ]
        for item in loader.get_all_entry_points():
            if item.is_reversible:
                name = item.__qualname__
                try:
                    self.invertibles[name] = (item(), item(reverse=True))
                except Exception:
                    pass

    def test_reversible(self):
        self.assertFalse(neg.is_reversible)
        self.assertTrue(b64.is_reversible)

    def test_reverse_property_random(self):
        for name, (convert, invert) in self.invertibles.items():
            if name in self.exceptions:
                continue
            for size in (0x40, 0x100, 0x200, 0x500):
                buffer = self.generate_random_buffer(size)
                self.assertEqual(buffer, convert(invert(buffer)))

    def test_reverse_property_structured(self):
        for name, (convert, invert) in self.invertibles.items():
            if name in self.exceptions:
                continue
            for buffer in self.structured_buffers:
                self.assertEqual(buffer, convert(invert(buffer)))
