from django.test import SimpleTestCase ,TestCase
from django.urls import reverse

# Create your tests here.

class TicketPageTests(TestCase):
    def test_url_exist_at_correct_location(self):
        response= self.client.get("/flights/")
        self.assertEqual(response.status_code , 200)

    def test_url_avalable_by_name(self):
        response= self.client.get(reverse('flight_list'))    
        self.assertEqual(response.status_code , 200)

    def test_template_name(self):
        response= self.client.get(reverse('flight_list'))  
        self.assertTemplateUsed(response , 'flight_list.html')  

      
