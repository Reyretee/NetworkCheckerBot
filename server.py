import asyncio
from handlers.ping_handler import PingHandler

async def handle_client(reader, writer, ping_handler, logger):
    try:
        data = await reader.read(1024)
        message = data.decode('utf-8')
        ping_handler.process_ping_data(message)
    except Exception as e:
        logger.error(f"Veri işlenirken hata meydana geldi: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
    
async def start_async_server(host, port, ping_handler, logger):
    server = await asyncio.start_server(
        lambda r, w: handle_client(r, w, ping_handler, logger),
        host, port
    )

    addrs = ', '.join(str(sock.getsockname())for sock in server.sockets)
    logger.info(f"{addrs} üzerinden gelen veriler izleniyor...")

    async with server:
        await server.serve_forever()