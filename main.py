import aiofiles
import asyncio
import json
import os
from pathlib import Path

async def main():
    async with aiofiles.open("articuno.json", mode='r') as f:
        contents = await f.read()
    pokemon = json.loads(contents)
    print(pokemon['name'])

async def read_lines():
    async with aiofiles.open('articuno.json', mode='r') as f:
        async for line in f:
            print(line)

async def write_bytes_to_temp_files():
    async with aiofiles.tempfile.NamedTemporaryFile('wb+') as file:
        await f.write(b'Line1\n Line2')
        await f.seek(0)
        async for line in f:
            print(line)


async def create_temporary_directory():
    async with aiofiles.tempfile.TemporaryDirectory() as d:
        filename = os.path.join(d, "file.ext")

async def read_files(filename):
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
    print(contents)

async def read_json_file_line(filename):
    async with aiofiles.open(filename, mode='r') as f:
        async for line in f:
            print(line)

async def writing_to_files(filename):
    async with aiofiles.open(filename, mode='w') as f:
        await f.write('transform')

async def read_mode(filename):
    async with aiofiles.open('rhydon.json', mode='r') as f:
        contents = await f.read()

        # load it into a dictionary and create alist of moves
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [moves['move']['name'] for move in pokemon['moves']]

        # Open a new file to write the list of moves into
        async with aiofiles.open(f'{name}_moves.txt', mode='w') as f:
            await f.write('\n'.join(moves))


directory = 'directory/your/files/are/in'

async def main():
    pathlist = Path(directory).glob('*.json')

    for path in pathlist:
        async with aiofiles.open(f'{directory}/{path.name}', mode='r') as f:
            contents = await f.read()

        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        async with aiofiles.open(f'{directory}/{name}', mode='w') as f:
            await f.write('\n'.join(moves))

asyncio.run(read_lines())
