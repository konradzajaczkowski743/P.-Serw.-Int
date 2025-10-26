import asyncio

from container import Container


async def main():

    container = Container()
    service = container.service()
    await service.save_posts()

    query = input("Wpisz filtr: ")
    data = await service.filter_posts(query)
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
