import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '':
        return ''
    if p_message == 'hello':
        return 'Hello!'
    if p_message == 'fuck off':
        return 'THAT\'S MEAN!!!'
    if p_message == 'roll':
        return str(random.randint(1, 6))
    if p_message == 'roll2':
        return str(random.randint(2, 12))
    if p_message == ':(':
        return 'Cheer up friend :)'
    if p_message == ':)':
        return 'Whats got you happy, stay sad loser!!'
    if p_message == 'can\'t wait for barbie!':
        return 'Oppenheimer is better'
    if p_message == 'can\'t wait for oppenheimer!':
        return 'Barbie is better'
    if p_message == '!help':
        return '`Current commands: ?[message], hello, roll, roll2`'
    if p_message == '<@&878567361656004628>':
        return 'I\'ll be there in a second <3'
    if p_message == 'bruh':
        return 'https://tenor.com/view/criminal-fnaf-facial-recognition-test-william-afton-gif-23135210'
    if p_message == 'rock and stone':
        ras = ['Rock on!','Rock and Stone... Yeeaaahhh!','Rock and Stone forever!','ROCK... AND... STONE!','Rock and Stone!','For Rock and Stone!', 'We are unbreakable!', 'Rock and roll!', 'Rock and roll and stone!', 'That\'s it lads! Rock and Stone!', 'Like that! Rock and Stone!', 'Yeaahhh! Rock and Stone!', 'None can stand before us!', 'Rock solid!', 'Stone and Rock! ...Oh, wait...', 'Come on guys! Rock and Stone!', 'If you don\'t Rock and Stone, you ain\'t comin\' home!','We fight for Rock and Stone!', 'We rock!', 'Rock and Stone everyone!', 'Stone.', 'Yeah, yeah, Rock and Stone.', 'Rock and Stone in the Heart!', 'For Teamwork!', 'Did I hear a Rock and Stone?', 'Rock and Stone!', 'Rock and Stone, Brother!', 'Rock and Stone to the Bone!', 'For Karl!', 'Leave No Dwarf Behind!', 'By the Beard!']
        return random.choice(ras)
    if p_message == 'rock and stone!':
        ras = ['Rock on!','Rock and Stone... Yeeaaahhh!','Rock and Stone forever!','ROCK... AND... STONE!','Rock and Stone!','For Rock and Stone!', 'We are unbreakable!', 'Rock and roll!', 'Rock and roll and stone!', 'That\'s it lads! Rock and Stone!', 'Like that! Rock and Stone!', 'Yeaahhh! Rock and Stone!', 'None can stand before us!', 'Rock solid!', 'Stone and Rock! ...Oh, wait...', 'Come on guys! Rock and Stone!', 'If you don\'t Rock and Stone, you ain\'t comin\' home!','We fight for Rock and Stone!', 'We rock!', 'Rock and Stone everyone!', 'Stone.', 'Yeah, yeah, Rock and Stone.', 'Rock and Stone in the Heart!', 'For Teamwork!', 'Did I hear a Rock and Stone?', 'Rock and Stone!', 'Rock and Stone, Brother!', 'Rock and Stone to the Bone!', 'For Karl!', 'Leave No Dwarf Behind!', 'By the Beard!']
        return random.choice(ras)