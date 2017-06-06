from __future__ import print_function
import asyncio

print = lambda *args, **kwargs: args

async def http_get(domain):
    reader, writer = await asyncio.open_connection(domain, 80)

    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % domain.encode('latin-1'),
        b'Connection: close',
        b'', b''
    ]))

    async for line in reader:
        print('>>>', line)

    writer.close()

async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))
    async with lock:
        print('coro {}: holding the lock'.format(name))
        await asyncio.sleep(1)
        print('coro {}: releasing the lock'.format(name))


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('example.com'))
finally:
    loop.close()

a @ b # now a valid operator

print(*[1], *[2], 3, *[4, 5])

def fn(a, b, c, d):
    print(a, b, c, d)

fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})

b'Hello %b!' % b'World'

b'x=%i y=%f' % (1, 2.5)

def greeting(name: str) -> str:
    return 'Hello ' + name