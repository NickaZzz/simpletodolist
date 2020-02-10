from django.test import TestCase

from lists.models import Item, List


class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        firstItem = Item()
        firstItem.text = 'The first list item'
        firstItem.list = list_
        firstItem.save()

        secondItem = Item()
        secondItem.text = 'Item the second'
        secondItem.list = list_
        secondItem.save()

        savedList = List.objects.first()
        self.assertEqual(savedList, list_)

        savedItems = Item.objects.all()
        self.assertEqual(savedItems.count(), 2)

        firstSavedItem = savedItems[0]
        secondSavedItem = savedItems[1]
        self.assertEqual(firstSavedItem.text, 'The first list item')
        self.assertEqual(firstSavedItem.list, list_)
        self.assertEqual(secondSavedItem.text, 'Item the second')
        self.assertEqual(secondSavedItem.list, list_)
