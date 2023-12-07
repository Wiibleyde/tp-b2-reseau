import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')
        if not data:
            print(f"Client {addr!r} disconnected")
            break
        message = data.decode()
        print(f"Received {message!r} from {addr!r}")
        print(f"Send: Hello {addr!r}")
        writer.write(f"Hello {addr!r}".encode())
        await writer.drain()
    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 13337)
    addrs = ', '.join(str(s.getsockname()) for s in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())