from django.test import TestCase
from lists.models import Item

# Don't test constants
# Don't repeat yourself

class HomePageTest(TestCase):

    def get_text(self):
        text = 'A new list item'
        return text
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'item_text': self.get_text()})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, self.get_text())

    
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': self.get_text()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necesary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
    
    def test_display_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        text_one = 'The first (ever) list item'
        text_two = 'Item the second'

        first_item = Item()
        first_item.text = text_one
        first_item.save()
        
        second_item = Item()
        second_item.text = text_two
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, text_one)
        self.assertEqual(second_saved_item.text, text_two)
