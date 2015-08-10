# youtube_analytics

### For running the script, you have to do this in django shell:

```from analytics.parser import ParseChannel
obj = ParseChannel()

#### for initializing database
obj.initialize_db() # for initializing database

#### for inserting details of fetched channels
obj.insert_details() 

#### for fetching all channels inside the existing channels in the database.
obj.fetch_channels() ```

### To run infinetly to fill the database then do this.

```
>>> from analytics.parser import ParseChannel
>>> obj = ParseChannel()
>>> obj.initialize_db()
>>> e = True
>>> while e:
...     obj.insert_details()
...     obj.fetch_channels()
...     e = obj.infinite_loop()
... ```