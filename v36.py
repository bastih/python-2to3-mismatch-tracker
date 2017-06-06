from typing import List, Dict
import decimal

primes: List[int] = []

captain: str  # Note: no initial value!


class Starship:
    stats: Dict[str, int] = {}


1_000_000_000_000_000
0x_FF_FF_FF_FF

async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
    result = [i async for i in aiter() if i % 2]
    result = [await fun() for fun in funcs if await condition()]


name = "Fred"
f"He said his name is {name}."

width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"