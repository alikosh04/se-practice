import unittest
from booking import can_book


class BookingTests(unittest.TestCase):

    def test_touching_end_is_allowed(self):
        self.assertIs(can_book(660, 720, 540, False, [(600, 660)]), True)

    def test_overlap_is_rejected(self):
        self.assertIs(can_book(630, 690, 540, False, [(600, 660)]), False)

    def test_blocked_room_is_rejected(self):
        self.assertIs(can_book(660, 720, 540, True, [(600, 660)]), False)

    def test_exactly_two_hours_allowed(self):
        self.assertIs(can_book(720, 840, 540, False, [(600, 660)]), True)

    def test_over_two_hours_rejected(self):
        self.assertIs(can_book(720, 841, 540, False, [(600, 660)]), False)

    def test_starts_now_rejected(self):
        self.assertIs(can_book(540, 570, 540, False, [(600, 660)]), False)

    def test_zero_length_rejected(self):
        self.assertIs(can_book(700, 700, 540, False, []), False)

    def test_reversed_times_rejected(self):
        self.assertIs(can_book(750, 700, 540, False, []), False)

    def test_negative_start_rejected(self):
        self.assertIs(can_book(-1, 60, 0, False, []), False)

    def test_end_of_day_allowed(self):
        self.assertIs(can_book(1380, 1440, 540, False, []), True)

    def test_after_end_of_day_rejected(self):
        self.assertIs(can_book(1400, 1441, 540, False, []), False)

    def test_empty_existing_allowed(self):
        self.assertIs(can_book(700, 760, 540, False, []), True)

    def test_multiple_existing_bookings(self):
        existing = [(600, 660), (720, 780), (900, 960)]
        self.assertIs(can_book(740, 800, 540, False, existing), False)

    def test_existing_is_unchanged(self):
        existing = [(600, 660)]
        before = existing.copy()
        can_book(660, 720, 540, False, existing)
        self.assertEqual(existing, before)

    def test_inside_existing_rejected(self):
        self.assertIs(can_book(615, 645, 540, False, [(600, 660)]), False)

    def test_contains_existing_rejected(self):
        self.assertIs(can_book(570, 690, 540, False, [(600, 660)]), False)

    def test_touching_start_allowed(self):
        self.assertIs(can_book(570, 600, 540, False, [(600, 660)]), True)

    def test_returns_real_boolean(self):
        result = can_book(700, 760, 540, False, [])
        self.assertIs(type(result), bool)
    
    def test_rejected_result_is_real_boolean(self):
        result = can_book(630, 690, 540, False, [(600, 660)])
        self.assertIs(result, False)

    def test_blocked_result_is_real_boolean(self):
        result = can_book(700, 760, 540, True, [])
        self.assertIs(result, False)

    def test_existing_unchanged_after_rejection(self):
        existing = [(600, 660), (720, 780)]
        before = existing.copy()

        result = can_book(630, 690, 540, False, existing)

        self.assertIs(result, False)
        self.assertEqual(existing, before)

    def test_existing_unchanged_with_multiple_bookings(self):
        existing = [(600, 660), (720, 780), (900, 960)]
        before = existing.copy()

        result = can_book(800, 860, 540, False, existing)

        self.assertIs(result, True)
        self.assertEqual(existing, before)

    def test_empty_existing_remains_empty(self):
        existing = []
        result = can_book(700, 760, 540, False, existing)

        self.assertIs(result, True)
        self.assertEqual(existing, [])

    def test_rejected_result_has_bool_type(self):
        result = can_book(630, 690, 540, False, [(600, 660)])
        self.assertIs(type(result), bool)