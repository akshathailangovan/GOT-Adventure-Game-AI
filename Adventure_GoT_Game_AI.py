import time
import random


def print_pause(message_to_print, t=2):
    print(message_to_print)
    time.sleep(t)


def error_message():
    print_pause("\nSorry! Please select from one of the choices above.\n", 2)


def initialization():
    print_pause("\n>>>>>>>INITIALIZING GAME SEQUENCE>>>>>>>>>>>>\n", 5)


def reboot():
    print_pause("\n>>>>>>>REBOOTING GAME SEQUENCE>>>>>>>>>>>>>>>\n", 5)


def play_again(items, segment):
    while True:
        play = input("Would you like to play again?(y/n)\n")
        if play.lower() == 'y':

            def replay_choice():
                print_pause("\nPress:\n [1] to replay this segment", 2)
                print_pause(" [2] to start over.\n", 2)
                play = input("Please enter your choice:\n")
                if play == '1':
                    replay_segment(items, segment)
                elif play == '2':
                    reboot()
                    play_game()
                else:
                    error_message()
                    replay_choice()
            replay_choice()
            break
        elif play.lower() == 'n':
            print_pause("\nUntil our paths cross again.\n", 2)
            print_pause("VALAR MORGHULIS!\n", 2)
            break
        else:
            error_message()
            play_again(items, segment)
            break


def replay_segment(items, segment):
    if segment == "braavos":
        arya(items)
    elif segment == "marketplace":
        initialization()
        save_ned(items)
    elif segment == "cartride":
        initialization()
        arya_run(items)
    elif segment == "fightinjury":
        initialization()
        arya_run(items)
    elif segment == "final":
        initialization()
        neds_execution(items)
    elif segment == "carcass":
        north(items)
    elif segment == "serpent":
        initialization()
        elixir(items)
    elif segment == "elixir":
        initialization()
        elixir(items)
    elif segment == "nomercy":
        initialization()
        elixir(items)
    elif segment == "dragon":
        initialization()
        dice(items)
    elif segment == "queen":
        initialization()
        dice(items)


def endings(sequence):
    if sequence == "braavos":
        print_pause("\n\"An offering to the God of Death??\"")
        print_pause("Jaqen H\'ghar exclaims.")
        print_pause("\nYou have already gulped the poisoned water.", 4)
        print_pause("\nYou should have known better.\n")
        initialization()
        print_pause("You are now eternalized in the HALL OF FACES.\n")
    elif sequence == "marketplace":
        print_pause("\nYou continue to stay hiding.")
        print_pause("\nThe guards discover your hiding place.", 4)
        initialization()
        print_pause("They find you and take you to King Joeffry.", 4)
        print_pause("\nHe orders your execution along with Ned Stark.\n", 4)
    elif sequence == "cartride":
        print_pause("\nYou decide to stay hiding until the cart stops.")
        print_pause("The cart finally screeches to a halt.")
        print_pause("\nThe men come to unload the huge jars")
        print_pause("\nThey spot you there!", 4)
        initialization()
        print_pause("\n\"It\'s her!\" one of them exclaims.")
        print_pause("\nThey turn you in to the guards.")
        print_pause("\nYou are now imprisoned in the DARK DUNGEONS.", 4)
    elif sequence == "fightinjury":
        initialization()
        print_pause("The execution of Ned Stark takes place before you.")
        print_pause("A SECOND TIME!", 4)
    elif sequence == "final":
        print_pause("You transmorph into Sir Ilyn Payne.\n", 4)
        print_pause("You kill Joeffry instead and save Ned Stark!", 4)
        initialization()
        print_pause("\nNed Stark manages to escape & return to Winterfell.", 5)
        print_pause("\nLater on, the Starks ally with the rest of Westeros.")
        print_pause("\nGathering troops, war is declared on the South.", 4)
        print_pause("\nThe Lannisters are defeated.")
        print_pause("\nNed Stark ascends the IRON THRONE.", 4)
        print_pause("\nPEACE IS RESTORED IN THE SEVEN KINGDOMS...", 4)
        print_pause("Atleast until the White Walkers cross the wall!", 4)
    elif sequence == "carcass":
        print_pause("\nYou may be the King beyond the Wall.")
        print_pause("\nBut to the first Wildlings, you are an intruder.", 4)
        print_pause("\nThe Wildlings deny asylum.", 4)
        initialization()
        print_pause("\nA deadly blizzard strikes that night.")
        print_pause("You are left to fend for yourself in the cold.", 4)
        print_pause("\nYou are frozen in time.")
        print_pause("\nJust NOT how you wanted to be!", 4)
    elif sequence == "serpent":
        print_pause("\n\"A choice of brawn... a poor one indeed. ")
        print_pause("You do no nothing, Jon Snow!\" the Serpent hisses.")
        print_pause("\nHer grip around you tightens.", 4)
        initialization()
        print_pause("\nAs you struggle, she strikes her fatal blow.")
        print_pause("\nPOISONING YOU!", 4)
    elif sequence == "elixir":
        print_pause("\n\"I bring the ELIXIR OF HOPE.\"you declare.\n", 4)
        print_pause("\"On behalf of the living that walk this earth,")
        print_pause("Faith is what I ask. One chance.")
        print_pause("Before you plague humanity with Death!\" you plead.", 4)
        initialization()
        print_pause("\nThe Children of the Forest drop the dragon glass")
        print_pause("\nThey set the First Man free.", 4)
        print_pause("\nThis time, you have not only proved yourself...")
        print_pause("A worthy King beyond the Wall but to all of humanity!!")
        print_pause("\n\nYou are THE AZOR AHAAI!", 5)
        print_pause("\nPEACE REIGNS IN THE SEVEN KINGDOMS...", 4)
        print_pause("\nAtleast until humans fight for power again!", 4)
    elif sequence == "nomercy":
        print_pause("\nYou stand stunned by the truth in their claim.", 4)
        print_pause("\nThe children of the Forest let go of the First Man.", 4)
        initialization()
        print_pause("\nThey capture you.")
        print_pause("\nThey plunge the dragonglass in your heart INSTEAD!", 4)
        print_pause("You are the new NIGHT KING!", 4)
    elif sequence == "dragon":
        initialization()
        print_pause("\nYou have no sword or armour.")
        print_pause("\nYou are burned down to ASHES!", 4)
    elif sequence == "queen":
        print_pause("\nYour armour protects you from the fire.")
        print_pause("\nYou brandish your sword.")
        print_pause("\nThe mesmerised dragons make way for you.", 4)
        initialization()
        print_pause("\nThe Dragon Queen sits inside in all her glory.")
        print_pause("There is an instant connection.", 4)
        print_pause("\n\"To what do I owe this honour, o King?\" she asks.", 4)
        print_pause("\n\"I come with insight into the future, my Queen.")
        print_pause("Beyond lies a power-thirsty world tainted by war.")
        print_pause("Here in Essos, you hold a home in people that adore you.")
        print_pause("Reconsider your endeavour beyond and yonder, my Queen.\"")
        print_pause("You present your case.", 4)
        print_pause("\n\"I shall reconsider,")
        print_pause("Only if you agree to stay.\" she concludes.", 4)
        print_pause("You agree to stay.", 4)
        print_pause("\nWith time, the fondness in your hearts grow.")
        print_pause("It concludes in a peaceful union through marriage.", 4)
        print_pause("\nAs two competent, just rulers, you rule wisely.", 4)
        print_pause("\nPEACE AND LOVE REIGN!", 4)
    print_pause("\nTHE END\n", 5)


def intro():
    print_pause("\n*********ALTERNATE ENDINGS - GoT Edition**********\n\n")
    print_pause("Winter has come! And GoT has come to an end.")
    print_pause("Book fans: I see you! :P\n")
    print_pause("But don\'t we all wish things ended differently?")
    print_pause("\n\nWhat would you change if you could?\n")
    print_pause("First, let\'s find out who you really are.\n")


def character_selection(items):
    while True:
        print_pause("\n>>>>>>>INITIALIZING CHARACTER SELECTION>>>>>>\n", 5)
        got_character = random.choice(["Arya", "Jon"])
        if got_character == "Arya":
            print_pause("You are ARYA STARK!")
            arya(items)
            break
        elif got_character == "Jon":
            print_pause("You are JON SNOW!")
            jon(items)
            break
        else:
            error_message()
            character_selection(items)
            break


def arya(items):
    initialization()
    print_pause("You have just arrived in the Free City of Braavos.")
    print_pause("\nPeople begin to recognise you as the Night King Slayer.")
    print_pause("\nYou make your way to the House of Black and White.\n", 4)
    print_pause("Jaqen H\'ghar greets you.")
    print_pause("He bellows,\"If it isn't Arya Stark of Winterfell?")
    print_pause("May I interest you in a drink?\"", 4)
    print_pause("\nHe plunges a chalice in the pool.")
    print_pause("He holds it up for you to drink.", 4)
    aryas_chalice(items)


def aryas_chalice(items):
    while True:
        drink = input("\nDo you accept?(y/n)\n")
        if drink.lower() == 'n':
            print_pause("\n\"As well ask what good is life,")
            print_pause("What good is death?\", you exclaim.", 4)
            print_pause("\n\"Old tricks never lose charm, eh?")
            print_pause("To old times and new!\" Jaqen H\'ghar retorts.")
            print_pause("He tosses the chalice away.\n", 4)
            print_pause("You have passed the test!!!\n", 4)
            print_pause("Jaqen H\'ghar leads you to the Hall of Faces.\n", 4)
            arya_timecloud(items)
            break
        elif drink.lower() == 'y':
            endings("braavos")
            play_again(items, "braavos")
            break
        else:
            error_message()
            aryas_chalice(items)
            break


def arya_timecloud(items):
    print_pause("The ground around you begins to rumble...\n", 5)
    print_pause("\"Your visit shall meet its true purpose.")
    print_pause("Behold! The Time Cloud!")
    print_pause("You\'ll be able to go back in time and change one thing. \"")
    print_pause("Jaqen H\'ghar gestures turning around.\n", 4)
    print_pause("In a fury, everything around you fades away.\n", 4)
    print_pause("The time cloud takes you back in time.")
    print_pause("You can transform the face of history as you know it.")
    print_pause("\nWhere are you off to?\n", 4)
    print_pause("You\'ll find out!\n", 4)
    initialization()
    save_ned(items)


def save_ned(items):
    print_pause("\n*********RESCUING THE HAND**********\n\n", 5)
    print_pause("The sun is burning down on King's Landing ruthlessly.")
    print_pause("The market place is abuzz in anticipation.")
    print_pause("It\'s the public trial of Ned Stark!\n", 4)
    print_pause("\"Do you think the Hand's guilty?\" Gendry wonders.")
    print_pause("He meticulously sharpens your sword, Needle.", 4)
    print_pause("\nBefore you can answer, you hear loud footsteps.\n", 5)
    print_pause("Quick!\n")
    arya_marketplace(items)


def arya_marketplace(items):
    print_pause("Press:\n [1] to duck and hide.")
    print_pause(" [2] to leave quickly.\n")

    def arya_hide(items):
        needle = input("Please enter your choice:\n")
        if needle == '1':
            print_pause("\nYou duck and hide.", 4)
            print_pause("\nMembers of the Kingsguard barge in as you cower.")
            print_pause("As you sift, you accidently knock off a hammer.")
            print_pause("\nYou cup your mouth and try not to gasp.\n")
            print_pause("A rat squeals and jumps out of nowhere.")
            print_pause("This distracts the guardsmen.\n", 5)

            def aryas_escape(items):
                print_pause("Press:\n [1] to continue hiding.")
                print_pause(" [2] to make a run for it.\n")
                needle = input("Please enter your choice:\n")
                if needle == '1':
                    endings("marketplace")
                    play_again(items, "marketplace")
                elif needle == '2':
                    arya_run(items)
                else:
                    error_message()
                    aryas_escape(items)
            aryas_escape(items)
        elif needle == '2':
            arya_run(items)
        else:
            error_message()
            arya_hide(items)
    arya_hide(items)


def arya_run(items):
    print_pause("\nYou make a run for it!\n", 4)
    print_pause("You chance upon your sword, Needle.")
    aryas_needle(items)
    print_pause("A cloud of dust rises as a horse cart approaches.")
    print_pause("It halts abruptly close to you.", 4)
    print_pause("You hear the men whisper, \"...Off to the Sept of Baelor!\"")
    print_pause("That is where the execution is about to happen!\n", 5)
    arya_cartride(items)


def aryas_needle(items):
    needle = input("Do you grab it? (y/n):\n")
    if needle == 'y':
        items. append("Needle")
        print_pause("\nYou have grabbed Needle.")
        print_pause("You have made it out unscathed.\n", 5)
    elif needle == 'n':
        print_pause("\nYou have managed to make it out of unscathed.")
        print_pause("But you don't have Needle with you.\n", 5)
    else:
        error_message()
        aryas_needle(items)


def arya_cartride(items):
    print_pause("\nPress:\n [1] to jump onto the cart and hide.")
    print_pause(" [2] to stay put.\n")
    cart = input("Please enter your choice:\n")
    if cart == '1':
        print_pause("\nYou have jumped onto the cart.")
        print_pause("You hid yourself behind the big jars.", 5)
        print_pause("\nThe cart begins to slow down.")
        print_pause("The Sept of Baelor comes into view.\n", 4)

        def aryas_escape():
            print_pause("Press:\n [1] to get off now.")
            print_pause(" [2] to stay hiding.\n")
            cart = input("Please enter your choice:\n")
            if cart == '1':
                print_pause("\nYou get off the cart.")
                print_pause("\nYou disappear into the crowd.")
                neds_execution(items)
            elif cart == '2':
                endings("cartride")
                play_again(items, "cartride")
            else:
                error_message()
                aryas_escape()
        aryas_escape()
    elif cart == '2':
        aryas_fight(items)
    else:
        error_message()
        arya_cartride(items)


def aryas_fight(items):
    print_pause("You decide not to hop onto the cart.")
    print_pause("\nYou keep walking.")
    print_pause("\nA couple of guards have caught up to you.", 4)
    print_pause("\nYou can\'t outrun them.")
    print_pause("So you decide to tackle them.", 4)
    if "Needle" in items:
        print_pause("\nYou quickly reach for Needle.")
        print_pause("\nA quick but intense combat ensues.", 5)
        print_pause("\nYou emerge victorious!!", 4)
        print_pause("\nYou leave for the Sept of Baelor.", 4)
        neds_execution(items)
    else:
        print_pause("\nYou do not have Needle with you.")
        print_pause("You valiantly attack them with your bare hands.\n", 4)
        print_pause("However, one of them plunges a sword in your gut\n", 4)
        print_pause("You are hurt severely.", 4)
        print_pause("\nBut you manage to fight back.")
        print_pause("You leaving them both writhing on the ground.")
        print_pause("\nYou are not one to give up.")
        print_pause("\nLimping, you still attempt to get to the execution.", 4)
        print_pause("\nDo you make it?\n", 4)
        print_pause("\nYou make it to the Sept of Baelor.\n", 4)
        print_pause("But you are too late!!!\n", 4)
        endings("fightinjury")
        play_again(items, "fightinjury")


def neds_execution(items):
    print_pause("\nYou have arrived at the Sept of Baelor.")
    print_pause("\nPeople have gathered anxiously for the impending trial.\n")
    print_pause("\nYou see your father being brought in chained.")
    print_pause("\nYour heart sinks.")
    print_pause("\nKing Joeffry orders Sir Ilyn Payne to execute Ned Stark.")
    print_pause("\n A collective gasp spreads across the crowd.\n")
    print_pause("Now's your turn. What do you do?\n", 4)
    aryas_final(items)


def aryas_final(items):
    print_pause("Press:\n [1] to work your magic")
    print_pause(" [2] to stay where you are\n")
    execute = input("Please enter your choice:\n")
    if execute == '1':
        endings("final")
        play_again(items, "final")
    elif execute == '2':
        endings("fightinjury")
        play_again(items, "fightinjury")
    else:
        error_message()
        aryas_final(items)


def jon(items):
    initialization()
    print_pause("You are standing at literal crossroads.")
    print_pause("Tyrion Lannister also stands by you.\n", 4)
    print_pause("An old friend, he takes the liberty to enlighten you.\n")
    print_pause("\"Behold the magical realm to the past!")
    print_pause("It has stayed hidden and protected for years.\"")
    print_pause("He says pointing at the two paths before you.", 4)
    print_pause("\n\"One leads you towards Ice and the other Fire.")
    print_pause("Flip a coin if you must, but choose wisely.")
    print_pause("And as I always say, bastard, never forget what you are.")
    print_pause("The rest of the world will not.")
    print_pause("Wear it like armor,")
    print_pause("And it can never be used to hurt you.\"\n", 5)
    print_pause("Have you made your decision?\n", 2)
    direction(items)


def direction(items):
    print_pause("Press:\n [1] to head North towards ICE")
    print_pause(" [2] to head East towards FIRE\n", 2)
    route = input("Please enter your choice:\n")
    if route == '1':
        north(items)
    elif route == '2':
        east(items)
    else:
        error_message()
        direction(items)


def north(items):
    initialization()
    print_pause("\"The North! Nothing like home.\"")
    print_pause("You exclaim decidedly as you bid adieu to Tyrion.", 4)
    print_pause("\nWhat follows is a tedious journey beyond the Wall.", 4)
    print_pause("\nYou stop to collect firewood before nightfall.")
    print_pause("\nYour direwolf, Ghost, prancing ahead starts howling.", 4)
    print_pause("\nYou follow Ghost.")
    print_pause("You find the fresh carcass of a dead animal.")
    print_pause("\nWhat do you do?\n", 4)
    carcass(items)
    print_pause("You notice smoke rising at a distance.")
    print_pause("Perhaps there are some human settlements nearby.\n", 4)
    print_pause("You walk towards the smoke.")
    print_pause("The earliest of Wilding settlements come into view.\n", 4)
    wildlings(items)


def carcass(items):
    print_pause("Press:\n [1] to collect the carcass.")
    print_pause(" [2] to leave it be.\n")
    collect = input("Please enter your choice:\n")
    if collect == '1':
        print_pause("\nYou pick up the carcass.\n", 4)
        items.append("carcass")
    elif collect == '2':
        print_pause("You decide to continue walking without it.", 4)
    else:
        error_message()
        carcass(items)


def wildlings(items):
    print_pause("\nYou could request the Wildlings for asylum.\n")
    if "carcass" in items:
        print_pause("You offer the animal carcass as a peace offering.")
        print_pause("The Chief is impressed by the offering.")
        print_pause("The Wildlings welcome you into their settlement.")
        print_pause("You are warmed by their hospitality.")
        print_pause("You broach the intent of your expedition.", 4)
        print_pause("\n\"I need to stop the Children of the Forest!")
        print_pause("From creating the White Walkers!\" you declare.", 4)
        print_pause("\n\"Not without the ELIXIR OF HOPE, my friend!")
        print_pause("It is guarded by the two-headed serpent.")
        print_pause("In a cave in the Black Ranges.\" the Chief advises.", 4)
        print_pause("\n\"My people will bring you to the foothills,")
        print_pause("Beyond which you are on your own.\" he offers.", 4)
        print_pause("\nA red-haired woman and a burly,bearded man escort you.")
        print_pause("You feel at home right away.\n", 4)
        print_pause("Days pass traversing the difficult terrain.", 4)
        print_pause("You have arrive at the foothills of the Black ranges.", 4)
        print_pause("\nTime has come to part ways with your dear friends.")
        elixir(items)
    else:
        endings("carcass")
        play_again(items, "carcass")


def elixir(items):
    print_pause("\nAfter a steep climb, you discover the cave.", 4)
    print_pause("\nAs you enter, a magnificently huge creature appears")
    print_pause("The two-headed serpent takes you into her fold.")
    print_pause("\nWhat do you do?\n", 4)

    def serpent(items):
        print_pause("Press:\n [1] to strike her.")
        print_pause(" [2] to initiate a word.\n")
        action = input("Please enter your choice:\n")
        if action == '1':
            endings("serpent")
            play_again(items, "serpent")
        elif action == '2':
            print_pause("\n\"I have come to transcend,")
            print_pause("The throes of history,")
            print_pause("As the world shall know it.")
            print_pause("Do you stand by me or in my way?\"")
            print_pause("You ask.", 4)
            print_pause("\n\"That depends, o King beyond the Wall!\"")
            print_pause("The serpent hisses.")
            print_pause("\"Dignify my conundrum with a response.")
            print_pause("And we shall find out!\"\n", 4)
            riddle(items)
        else:
            error_message()
            serpent(items)
    serpent(items)


def riddle(items):
    print_pause("\nYou nod in agreement as she continues,\n\n")
    print_pause(" \"Truly no one is outstanding without me,")
    print_pause("   nor fortunate; I embrace all those whose hearts")
    print_pause("   Ask for me.")
    print_pause("   He who goes without me")
    print_pause("   Goes about in the company of death;")
    print_pause("   And he who bears me will remain lucky for ever.")
    print_pause("   But I stand lower than earth")
    print_pause("   And higher than heaven.\"\n", 5)
    print_pause("Press:\n [1] to respond WISDOM.")
    print_pause(" [2] to respond PATIENCE.")
    print_pause(" [3] to respond HAPPINESS.")
    print_pause(" [4] to respond HUMILITY.")
    answer = input("\nPlease enter your choice:\n")
    if answer == '4':
        print_pause("\n\"Spoken like a true King!")
        print_pause("Tales from far and high I have heard many.")
        print_pause("But today I bear witness to your prowess.\"")
        print_pause("The Serpent exclaims.", 4)
        print_pause("\n\"The ELIXIR OF HOPE is yours!\"\n", 4)
        print_pause("\nA glimmering ray of blinding light emerges.", 4)
        print_pause("\nCollecting the ELIXIR OF HOPE, you leave the cave.", 4)
        items.append("Elixir")
        print_pause("\nOutside the cave, the cold winter winds have halted.")
        print_pause("Grass has turned green.")
        print_pause("Flowers are in full bloom.", 4)
        forest_children(items)
    elif answer == '1' or answer == '2' or answer == '3':
        print_pause("\n\"Wrong! I expected a world better of you, o King!")
        print_pause("The ELIXIR OF HOPE shall remain in my keep.\"")
        print_pause("The Serpent hisses.", 4)
        print_pause("\nYou leave the cave without the ELIXIR OF HOPE.", 4)
        print_pause("\nYou look for the Children of the Forest anyway.", 4)
        forest_children(items)


def forest_children(items):
    print_pause("\nThe Children of the Forest prepare to plunge")
    print_pause("Dragonglass in the heart of a First Men")
    print_pause("to create the first ever White Walker, the Night King.", 4)
    print_pause("\n\"STOP!!\" you shout out to them.", 4)
    print_pause("\n\"Pray... Tell us why?!\" one of them rasps.")
    print_pause("\"Even Death can be defeated,")
    print_pause(" As you of all may know.")
    print_pause(" But can human depravity,")
    print_pause(" That greedily craves power?\"\n", 4)
    if "Elixir" in items:
        endings("elixir")
        play_again(items, "elixir")
    else:
        endings("nomercy")
        play_again(items, "nomercy")


def east(items):
    initialization()
    print_pause("\n\"East, it is!\" you declare.")
    print_pause("You part ways with Tyrion.", 4)
    print_pause("\nMonths go by in a perilous sea voyage.")
    print_pause("You finally arrive at Essos.", 4)
    print_pause("\nYou walk the streets of Meereen cautiously.", 4)
    print_pause("\nA child appears out of nowhere.")
    print_pause("She runs away with your sword, Long Claw.", 4)
    print_pause("\nYou chase the child to a crowded square.")
    print_pause("People have gathered to witness the oracle of the Red Woman.")
    print_pause("\nThe Red Woman chants a high-pitched sermon.")
    print_pause("She places your sword, Long Claw, on an ivory rack.", 4)
    dice(items)


def dice(items):
    print_pause("\n\"A game of fate shall determine,")
    print_pause("Long Claw to its rightful owner.\" she proclaims.", 4)
    print_pause("\n\"YOU! I see you are here to fulfill your destiny.\"")
    print_pause("She points to you.", 4)
    print_pause("\n\"Pick a number(1-6) and roll the dice.")
    print_pause("A match will win you back your sword!\"\n", 4)
    print_pause("Remember, these dice are skewed to favor odd numbers.")
    number = input("Please enter your choice:\n")
    dice = random.choice([1, 3, 5])
    if int(number) == dice:
        print_pause("\"A MATCH! The God of Light has spoken!")
        print_pause("You are the AZOR AHAAI!")
        print_pause("Take everything that is yours.\"")
        print_pause("The Red Woman announces.", 4)
        items. append("Longclaw")
        print_pause("\n\"Accept with it this armour,")
        print_pause("That shall protect you from everything even FIRE.\"")
        print_pause("she claims.", 4)
        items. append("armour")
        print_pause("\nThe news of your arrival spreads across Meereen.")
        print_pause("You are summoned by the Queen, Daenerys Targaryen.", 4)
        court(items)
    else:
        print_pause("\"Not a match! Longclaw stays here.")
        print_pause("Begone, o King!\" the Red Woman declares.\n", 4)
        print_pause("You head to the Great Pyramid anyway.\n", 4)
        court(items)


def court(items):
    print_pause("\nThe entrance to the Great Pyramid is guarded.")
    print_pause("By the mighty children of the Queen, the Dragons.", 4)
    print_pause("\nDrogon swoops right in and spits a ball of fire.", 4)
    if "Longclaw" and "armour" in items:
        endings("queen")
        play_again(items, "queen")
    else:
        endings("dragon")
        play_again(items, "dragon")


def play_game():
    items = []
    intro()
    character_selection(items)
    print("\n")


play_game()
