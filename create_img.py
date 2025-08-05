from PIL import Image, ImageDraw, ImageFont
import random
import textwrap


# Load the background image (your custom backdrop)
background = Image.open("assets/placeholder_avatar.png").convert("RGBA")

# List of costs
fftcg_costs = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

# List of elements
elements = ["Wind", "Earth", "Lightning", "Fire", "Ice", "Water", "Light", "Dark"]

# List of jobs
fftcg_jobs = [
    "Warrior",
    "Knight",
    "Dragoon",
    "Dark Knight",
    "Paladin",
    "Monk",
    "Samurai",
    "Ninja",
    "Thief",
    "Assassin",
    "Ranger",
    "Hunter",
    "Archer",
    "Red Mage",
    "Black Mage",
    "White Mage",
    "Blue Mage",
    "Time Mage",
    "Summoner",
    "Scholar",
    "Sage",
    "Geomancer",
    "Dancer",
    "Bard",
    "Machinist",
    "Gunner",
    "Engineer",
    "Alchemist",
    "Beastmaster",
    "Mystic Knight"
]

# List of types
fftcg_types = [
    "Forward",
    "Backup",
    "Summon",
    "Monster",
]

# List of categories
category = "Twitch"

# List of power values
fftcg_power = [
    "2000", "3000", "4000", "5000", "6000", "7000", "8000", "9000", "10000"
]

# List of abilities
forward_abilities = [
    "This Forward gains Brave as long as you control a Backup of the same element.",
    "When this Forward enters the field, choose 1 Forward. Dull it.",
    "This Forward gains +1000 power for each card in your hand.",
    "When this Forward attacks, you may pay 1 CP. If you do, it gains First Strike until end of turn.",
    "If this Forward is dealt damage, reduce that damage by 2000.",
    "When this Forward is blocked, deal 3000 damage to the blocking Forward.",
    "This Forward cannot be chosen by your opponent’s Summons or abilities.",
    "When this Forward enters the field, you may search your deck for a Job card and add it to your hand.",
    "If this Forward is put into the Break Zone, you may pay 2 CP. If you do, return it to your hand.",
    "This Forward gains Haste if you control a character with the same Job.",
    "When this Forward enters the field, choose 1 Backup. Activate it.",
    "This Forward gains +3000 power if you control a character with the same name.",
    "When this Forward attacks, your opponent discards 1 card from their hand.",
    "If this Forward deals damage to a Forward, break that Forward.",
    "This Forward gains First Strike and Brave during your turn.",
    "When this Forward is chosen by an ability, draw 1 card.",
    "If this Forward is put into the Break Zone, choose 1 Forward. Deal it 7000 damage.",
    "This Forward cannot be blocked by Forwards with a different element.",
    "When this Forward enters the field, reveal the top card of your deck. If it’s a Forward, add it to your hand.",
    "This Forward gains Haste and cannot be chosen by opponent’s abilities if you control 5 or more characters.",
    "When this Forward enters the field, choose 1 Forward. It loses 2000 power until end of turn.",
    "This Forward gains +1000 power for each different element among characters you control.",
    "When this Forward attacks, choose up to 2 Forwards. Dull them.",
    "If this Forward is blocked, deal 5000 damage to the blocking Forward.",
    "This Forward gains Haste if you control a Backup of the same Job.",
    "When this Forward is put into the Break Zone, you may pay 1 CP. If you do, draw 1 card.",
    "This Forward gains First Strike if you control 2 or more Backups.",
    "When this Forward enters the field, choose 1 Forward. Freeze it.",
    "This Forward cannot be broken by damage less than 8000.",
    "When this Forward attacks, you may search your deck for a card with the same Job and add it to your hand."
]

# List of abilities for backups
backup_abilities = [
    "When this Backup enters the field, draw 1 card.",
    "Dull this Backup: Choose 1 Forward. It gains +1000 power until end of turn.",
    "Dull this Backup: Choose 1 Forward. It gains First Strike until end of turn.",
    "Dull this Backup: Choose 1 Forward. It gains Brave until end of turn.",
    "Dull this Backup: Choose 1 Forward. It gains Haste until end of turn.",
    "Dull this Backup: Choose 1 Forward. It cannot be chosen by opponent’s abilities this turn.",
    "Dull this Backup: Choose 1 Forward. It cannot be blocked this turn.",
    "Dull this Backup: Choose 1 Forward. It gains +2000 power if it shares an element with this Backup.",
    "When this Backup enters the field, choose 1 Forward. Dull it.",
    "When this Backup enters the field, choose 1 Forward. Activate it.",
    "Dull this Backup: Reveal the top card of your deck. If it’s a Forward, add it to your hand.",
    "Dull this Backup: Choose 1 Forward. It gains “If this Forward is put into the Break Zone, return it to hand.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward attacks, draw 1 card.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward blocks, deal 3000 damage to the attacker.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward cannot be broken by damage less than 7000.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward is chosen by an ability, draw 1 card.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward enters the field, activate all Backups.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward attacks, your opponent discards 1 card.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward deals damage, choose 1 Forward. Break it.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward is blocked, deal 5000 damage to the blocker.”",
    "Dull this Backup: Choose 1 Forward. It gains “When this Forward is put into the Break Zone, draw 2 cards.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward cannot be dulled by opponent’s abilities.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +1000 power for each Backup you control.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +2000 power if you control 3 or more elements.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains Haste and Brave if you control 5 characters.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains First Strike and cannot be blocked.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +3000 power if you control a character with the same Job.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +2000 power and cannot be chosen by Summons.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +1000 power and draws 1 card when it attacks.”",
    "Dull this Backup: Choose 1 Forward. It gains “This Forward gains +1000 power and cannot be broken this turn.”"
]

# List of abilities for summons
summon_texts = [
    "Choose 1 Forward. Deal it 7000 damage.",
    "Choose up to 2 Forwards. Dull them.",
    "Choose 1 Forward. Break it.",
    "Choose 1 Forward. It loses 4000 power until end of turn.",
    "Choose 1 Forward. Return it to its owner's hand.",
    "Choose 1 Forward. Freeze it.",
    "Choose 1 Forward. It cannot block this turn.",
    "Choose 1 Forward. It cannot be chosen by abilities until end of turn.",
    "Choose 1 Forward. It gains Haste and First Strike until end of turn.",
    "Choose 1 Forward. It gains +3000 power until end of turn.",
    "Choose 1 character. Activate it.",
    "Choose 1 Backup. Dull it.",
    "Choose 1 Forward. It gains “When this Forward attacks, draw 1 card.” until end of turn.",
    "Choose 1 Forward. It gains “When this Forward deals damage, break target Forward.” until end of turn.",
    "Choose 1 Forward. It gains “This Forward cannot be broken this turn.”",
    "Choose 1 Forward. It gains “This Forward cannot be blocked this turn.”",
    "Choose 1 Forward. It gains “When this Forward enters the field, deal 5000 damage to all Forwards.”",
    "Choose 1 Forward. It gains “When this Forward is put into the Break Zone, return it to hand.”",
    "Choose 1 Forward. It gains “This Forward gains +1000 power for each different element you control.”",
    "Choose 1 Forward. It gains “This Forward gains Brave and cannot be dulled this turn.”"
]

# List of abilities for monsters
monster_abilities = [
    "When you control 3 or more Backups, this Monster can become a Forward with 7000 power.",
    "Dull this Monster: Choose 1 Forward. It loses 2000 power until end of turn.",
    "When this Monster enters the field, choose 1 Forward. Freeze it.",
    "This Monster can attack as a Forward if you control a character with the same element.",
    "Dull this Monster: Choose 1 Forward. It cannot block this turn.",
    "This Monster cannot be chosen by opponent’s Summons or abilities.",
    "When this Monster is put into the Break Zone, draw 1 card.",
    "Dull this Monster: Choose 1 Forward. It gains +1000 power until end of turn.",
    "This Monster becomes a Forward with 8000 power if you control 2 or more Monsters.",
    "Dull this Monster: Choose 1 Forward. It gains First Strike until end of turn.",
    "This Monster gains “When this Monster attacks, your opponent discards 1 card.”",
    "This Monster becomes a Forward with 6000 power and Brave if you control a Backup of the same element.",
    "Dull this Monster: Choose 1 Forward. It gains “This Forward cannot be broken this turn.”",
    "This Monster gains “When this Monster is dulled, activate 1 Backup.”",
    "This Monster becomes a Forward with 9000 power if you control 5 or more characters.",
    "Dull this Monster: Choose 1 Forward. It gains “When this Forward attacks, deal 3000 damage to target Forward.”",
    "This Monster gains “When this Monster enters the field, search your deck for a Monster and add it to your hand.”",
    "This Monster becomes a Forward with 7000 power and Haste if you control a Forward with the same Job.",
    "Dull this Monster: Choose 1 Forward. It gains “This Forward cannot be dulled by opponent’s abilities.”",
    "This Monster gains “When this Monster is put into the Break Zone, choose 1 Forward. Break it.”"
]


def generate_card(background_image_path, twitch_username, output_path="static/card.png"):

    # Randomly select frame and attributes
    selected = random.choice(elements)
    filename = f"{selected}.png"
    frame = Image.open(f"frames/{filename}").convert("RGBA")
    background = Image.open(background_image_path).convert("RGBA").resize(frame.size)

    # Create drawing context
    draw = ImageDraw.Draw(frame)

    # Generate card attributes
    name = twitch_username
    cost = random.choice(fftcg_costs)
    type_ = random.choice(fftcg_types)
    job = random.choice(fftcg_jobs) if type_ in ["Forward", "Backup"] else ""
    ability = (
        random.choice(forward_abilities) if type_ == "Forward" else
        random.choice(backup_abilities) if type_ == "Backup" else
        random.choice(summon_texts) if type_ == "Summon" else
        random.choice(monster_abilities)
    )
    power = random.choice(fftcg_power) if type_ in ["Forward", "Monster"] else ""
    ability = textwrap.fill(ability, width=50)
    flavor_text = "© DaMaxicanJustice\nCharacter Illustration: Someone\nFinal Fantasy >0"

    # Load fonts
    extra_small = ImageFont.truetype("fonts/beleren.ttf", size=12)
    small = ImageFont.truetype("fonts/beleren.ttf", size=18)
    medium = ImageFont.truetype("fonts/beleren.ttf", size=24)
    large = ImageFont.truetype("fonts/beleren.ttf", size=56)

    # Draw text
    draw.text((46.5, 80), cost, font=large, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((125, 75), name, font=medium, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((300, 530), job, font=small, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((50, 530), type_, font=small, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((550, 510), category, font=extra_small, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((25, 575), ability, font=medium, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((460, 810), power, font=large, fill="white", stroke_fill="black", stroke_width=2)
    draw.text((25, 800), flavor_text, font=small, fill="white", stroke_fill="black", stroke_width=2)

    # Composite and save
    combined = Image.alpha_composite(background, frame)
    combined.save(output_path)

    return output_path
