import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

        

    # Test a Profile can add a favourite Movie
    def test_profile_can_add_favourite_movie(self):
        self.profile_1.add_movie(self.movie_1)
        self.assertEqual(1, len(self.profile_1.favourites))
    

    # Test a Profile can remove a given Movie from favourites
    def test_remove_movie_from_favourites(self):
        self.profile_1.add_movie(self.movie_1)
        self.profile_1.remove_movie(self.movie_1)
        self.assertEqual(0, len(self.profile_1.favourites))

    

   
