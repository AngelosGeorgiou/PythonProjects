# For this exercise you will be strengthening your page-fu mastery. You will
# complete the PaginationHelper class, which is a utility class helpful for
# querying paging information related to an array.

# The class is designed to take in an array of values and an integer
# indicating how many items will be allowed per each page. The types of values
# contained within the collection/array are not relevant.


# TODO: complete this class

class PaginationHelper:

	# The constructor takes in an array of items and a integer indicating
	# how many items fit within a single page
	def __init__(self, collection, items_per_page):
		self.list = collection
		self.pager = items_per_page


	# returns the number of items within the entire collection
	def item_count(self):
		return len(self.list)

	# returns the number of pages
	def page_count(self):
		return self.item_count()//self.pager+1

	# returns the number of items on the current page. page_index is zero based
	# this method should return -1 for page_index values that are out of range
	def page_item_count(self,page_index):
		return -1 if page_index>self.page_count() - 1 else self.pager if page_index<self.page_count() - 1 else self.item_count()%self.pager	

	#return the page's index which the item's index belongs
	def page_index(self,index):
		return -1 if index+1>self.item_count() or index<0 else  index//self.pager

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_ndex takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid
