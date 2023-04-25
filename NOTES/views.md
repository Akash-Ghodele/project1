Django view
-----------

What is a view in django?
    
    - consist of business logic
    - handles request made to the URL
    - django uses 2 kinds of views
        - function based view
        - class-based
            - generic view
            - custom view

    - DRF uses class based views
        - DRF has lot of reusable logic implemented
        - We can change behaviour by overriding default configuration.


- APIView
  - Focused around HTTP methods
  - class methods (HTTP methods / HTTP verbs)
    - GET, POST, PUT, DELETE, PATCH
    - method names in API view are derived from HTTP verbs
  - provides flexibility over logic

- Viewsets
  - Focus around actions
    - retrieve, list, update, partial update, destroy
  - Can map to django models
  - Great for performing CRUD operations on models