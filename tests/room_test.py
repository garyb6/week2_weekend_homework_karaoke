import unittest 

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Jay Pritchard", 6, 200.00)
        self.guest2 = Guest("Cameron Tucker", 3, 100.00)
        self.room1 = Room("Cheviot", 10, 50)
        self.room2 = Room("Braid", 5, 25)
        self.song1 = Song("Dance Dance", "Fall Out Boy")
        self.song2 = Song("Ridin' Solo", "Jason Derulo")

    def test_room_has_name(self):
        self.assertEqual("Cheviot", self.room1.name) 
    
    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity) 

    def test_room_has_entry_fee(self):
        self.assertEqual(50, self.room1.entry_fee) 

    def test_guest_list_starts_off_empty(self):
        self.assertEqual([], self.room1.guest_list)
    
    def test_playlist_starts_off_empty(self):
        self.assertEqual([], self.room1.playlist)

    def test_can_add_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guest_list))

    def test_room_find_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)        
        self.assertEqual(self.guest2, self.room1.find_guest_by_name("Cameron Tucker"))
        self.assertEqual(None, self.room1.find_guest_by_name("Homer Simpson"))

    def test_can_remove_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)  
        self.room1.remove_guest(self.guest2)
        self.assertEqual(1, len(self.room1.guest_list))
        self.assertEqual(False, self.guest2 in self.room1.guest_list)
    
    def test_can_add_songs_to_playlist(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.playlist))

    def test_room_find_song_by_title(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)      
        self.assertEqual(self.song2, self.room1.find_song_by_title("Ridin' Solo"))
        self.assertEqual(None, self.room1.find_song_by_title("Trumpets"))
    
    def test_room_find_song_by_artist(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)      
        self.assertEqual(self.song2, self.room1.find_song_by_artist("Jason Derulo"))
        self.assertEqual(None, self.room1.find_song_by_artist("Rick Astley"))
    
    def test_can_guest_enter_room(self): 
        self.room2.add_guest(self.guest2)
        self.assertEqual(True, self.guest2.group_size <= self.room2.capacity)
    
    def test_guest_cannot_enter_room(self):
        self.room2.add_guest(self.guest1)
        self.assertEqual(False, self.guest1.group_size <= self.room2.capacity)
    
    def test_remaining_capacity(self):
        self.room2.add_guest(self.guest2)
        self.assertEqual(2, self.room2.capacity - self.guest2.group_size)
    
    def test_guest_can_afford_room(self):
        self.room2.add_guest(self.guest2)
        self.assertEqual(True, self.guest2.wallet >= self.room2.entry_fee)

    
    # def test_can_guest_pays_entry_fee(self):
    #     self.room2.add_guest(self.guest2)
    #     self.assertEqual (75, self.guest2.wallet)
    #     self.assertEqual (125, self.room2.till)






