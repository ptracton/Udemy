# Dialog Categories
# By Intelligence
#     Dumb -- Widgets parent sets initial values, unaware of data it contains, no need for extra API code.  Tied to user interface and lack of ability to add complex verification
#     Standard -- Most used.  Set widgets to values via API.  Caller need not know implementation details.  Clutters code if there is a lot to handle
#     Smart -- Updates based on data references or structures passed to it.  Capable of updating data directly.  Usually Modeless.  little code involved.  risk of not interacting with main app
# By Modality
#     Application Mode -- Once invoked, it is the only part you can interact with, like an error dialog
#     Window Mode -- Prevent interaction with parent
#     Modeless -- You can still interact with the rest of the application, main up could update while this window is open
                  # will need to be aware of this
#