# Count Numbers
This script is pretty inefficient as of right now, so don't be surprised if you find it running for a while on larger numbers. I've went through the courtesy of running some large numbers. Here they are:

| Number   |  Time (in seconds) |
|----------|:------------------:|
| 10,000,000    |         65,288,902.8 (755.66 days)      |

## How to run
I reccomend you run this script on a remote server for larger numbers to reduce the amount of work your personal computer will do. For me, I just ssh-ed into the UWaterloo servers and ran it there.

Once you cloned the repo, access `count.py` and modify `NUMBER_TO_COUNT_TO` at the bottom of the file. Then, simply run
```python
python count.py
```
## Testing
To test, run
```python
python test-count-numbers.py
```
If no errors exist, you should see `"All tests passed."`; otherwise, an AssertionError will be shown.
