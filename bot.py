from pytz import timezone
import discord

clear_command = 'kliruj kurwo pierdolona'

swap_chars = {
    'ę': 'e',
}

ignored = [
    428876312506138625
]

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged in...\n')

        self.load()

    async def on_message(self, message):
        if self.should_ignore(message):
            return

        if self.should_clear(message):
            await self.clear(message)

            return

        if self.has_cursed(message):
            await self.occured(message)

            return
        
    def should_ignore(self, message):
        return message.author.id in ignored

    def should_clear(self, message):
        return message.content == clear_command and message.author.guild_permissions.administrator

    def has_cursed(self, message):
        content = message.content.replace(' ', '').lower()

        for key, char in swap_chars.items():
            content = message.content.replace(key, char)

        if ('japierdole' in content.lower()) or ('ja' in content.lower() and 'pierdole' in content.lower()):
            return True

        return False

    async def occured(self, message):
        self.increment()

        print('Occured!')
        print('[{}][{}]: {}\n'.format(message.created_at, message.author.name, message.content))

        await message.channel.send('pierdolnelo {0} raz'.format(self.occurs))

    async def clear(self, message):
        self.occurs = 0
        self.update(0)

        print('Cleared!\n')
        await message.channel.send('nie przeklinaj kurwiu')

    def load(self):
        # avoids error when data.txt isn't created yet
        try:
            data = open('data.txt', 'r')
            self.occurs = int(data.read())
            data.close()
        except:
            self.occurs = 0

    def increment(self):
        self.occurs += 1
        self.update(self.occurs)

    def update(self, updated):
        data = open('data.txt', 'w')
        data.write(str(updated))
        data.close()
