from django.test import TestCase
from .models import Event

class EventTestCase(TestCase):
    
    def test_createNewEvent(self):
        Event.objects.create(Category="Music", Title="Test Title1", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        theTestEvent1 = Event()
        theTestEvent1 = Event.objects.get(Title="Test Title1")
        #print(theTestEvent1)
        #print("the title")
        #print(theTestEvent.Title)
        self.assertEqual(theTestEvent1.Title, 'Test Title1')

        Event.objects.create(Category="Art and Performances", Title="Test Title2", Date="12-3-20", Times="6:00 p.m. - 9:00 p.m.", PictureLink="link", AdmissionFee="30", Description="test", Location="test", Phone="300", AgeRestriction="10", token1="10", token2="20", token3="30")
        theTestEvent2 = Event()
        theTestEvent2 = Event.objects.get(Date="12-3-20")
        #print(theTestEvent2)
        self.assertEqual(theTestEvent2.Date, '12-3-20')

    def test_GetAllParticularEvents(self):
        Event.objects.create(Category="Music", Title="Test Music Event 1", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Music", Title="Test Music Event 2", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Music", Title="Test Music Event 3", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        theParticularEvents = Event.objects.filter(Category='Music')

        self.assertEqual(len(theParticularEvents), 3)

        Event.objects.create(Category="Over the Weekend", Title="OTW Event 1", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Over the Weekend", Title="OTW Event 2", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Over the Weekend", Title="OTW Event 3", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Over the Weekend", Title="OTW Event 3", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        theParticularEvents = Event.objects.filter(Category='Over the Weekend')

        self.assertEqual(len(theParticularEvents), 4)

    def test_GetALLEvents(self):
        Event.objects.create(Category="Over the Weekend", Title="Test Event 1", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Music", Title="Test Event 2", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Art and Performances", Title="Test Event 3", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Health and Fitness", Title="Test Event 4", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")
        Event.objects.create(Category="Over the Weekend", Title="Test Event 5", Date="1-1-18", Times="1:00 a.m. - 2:00 p.m.", PictureLink="link", AdmissionFee="10", Description="test", Location="test", Phone="100", AgeRestriction="10", token1="1", token2="2", token3="3")

        allEvents = Event.objects.all()

        self.assertEqual(len(allEvents), 5)