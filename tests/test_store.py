import pytest
from app.models import IdeaRequest
from app.store import IdeaStore

def test_fresh_store_contains_two_seed_ideas():
    # A unit test: no web server or HTTP client.
    store = IdeaStore()
    assert len(store.find_all()) == 2

def test_adding_idea_stores_title_and_category():
    # Arrange: fresh store and IdeaRequest.
    store = IdeaStore()
    request = IdeaRequest(title="Test Title", category="Test Category")
    
    # Act: call add(request).
    idea = store.add(request)
    
    # Assert: returned title/category and find_all contains the idea.
    assert idea.title == "Test Title"
    assert idea.category == "Test Category"
    assert len(store.find_all()) == 3
    assert idea in store.find_all()

def test_two_new_ideas_receive_different_ids():
    # Arrange: fresh store. 
    store = IdeaStore()
    req1 = IdeaRequest(title="Idea 1", category="cat1")
    req2 = IdeaRequest(title="Idea 2", category="cat2")
    
    # Act: add two requests.
    idea1 = store.add(req1)
    idea2 = store.add(req2)
    
    # Assert: ids differ, do not reuse seed ids, list size is four.
    assert idea1.id != idea2.id
    assert idea1.id > 2  # Seed ids are 1 and 2
    assert idea2.id > 2
    assert len(store.find_all()) == 4
