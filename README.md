# SpeedList
Fast list search for validation of element presence and standard list-style entity storage and retrieval


SpeedList is a high-speed tool for management and boolean queries of extra large lists using a series of 36 "hydras" -- internally-maintained lists of md5 hashed keys with list elements values. Like alphabetizing, if you were insane. SpeedList was designed with web crawlers in mind where newly-harvested URLs are often checked against large "already crawled" URL lists, but is equally useful for any task that involves searching extra large lists. SpeedList also has a built-in ThreadPoolExecutor with customizable worker pool sizes.

## But how fast is it?

```
import SpeedList
import time

maker = SpeedList()

# Create a list of alphanumeric values, 30 characters per item for 1,000,000 items
dummy_list = maker.make_dummy(30, 1000000) # This takes forever and is only for this example

# Add a value to search for
dummy_list.append('dummy value')

# Initialize hydra using dummy list
hydra = maker.make_hydra(use=dummy_list)

# Rather unscientific speed test of standard list searching

start = time.time()
for _ in range(1000):
    if 'dummy value' in dummy_list:
        continue
print (f'Standard search cycle completed in {time.time() - start} seconds.')

> Stansard search cycle completed in 12.068743228912354 seconds.


# And the same test with SpeedList

start = time.time()
for _ in range(1000):
    if hydra.see('dummy value'):
        continue
print (f'SpeedList search cycle completed in {time.time() - start} seconds.')

>> SpeedList search cycle completed in 3.358163833618164 seconds.
```
