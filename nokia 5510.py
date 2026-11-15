main menu = """
List of menu function
    press 1 for phone book
    press 2 for messages
    press 3 for chat
    press 4 for call register
    press 5 for tones
    press 6 for settings
    press 7 for call divert
    press 8 for music
    press 9 for games
    press 10 for calculator
    press 11 for reminders
    press 12 for clock
    press 13 for profiles
    press 14 for services
    press 15 for sim services
    enter 0 to exit """
        print(main_menu)

    main_menu_list = int(input("main menu"))

    match main_menu_list:

        case 1:
            print("phone book")
        
        
    phone_book = """
    press 1 for search
    press 2 for service nos
    press 3 for add name
    press 4 for erase
    press 5 for edit
    press 6 for copy
    press 7 for assign tone
    press 8 for send b'card
    press 9 for options
    press 10 for speed dials
    press 11 for voice tags
    enter 0 to exit """
        print(pnone_book)
        phone_book_list = int(input("phone book"))
    
    match phone_book_list:
        case 1:
            print("search")
        case 2:
            print("service nos")
        case 3:
            print("add name")
        case 4:
            print("erase")
        case 5:
            print("edit")
        case 6:
            print("copy")
        case 7:
            print("assign tone")
        case 8:
            print("send b'card")
        case 9:
            print("options")
            
            option = """
            press 1 memory in use
            press 2 type of view
            press 3 memory status
            enter 0 to exit 
            """
            print(option)
            
            print(option_menu)
            option_menu_list = int(input("options"))
            
            match option_menu_list:
            case 1:
                print("memory in use")
            case 2:
                print("type of view")
            case 3:
                print("memory status")
            case 0: 
                break
            case _:
                print("invalid")
                
        case 10:
            print("speed dials")
        case 11:
            print("voice tags")
        case 0: 
        break
        case _:
            print("invalid")
        
        
        case 2:
            print("message")
            
    message = """
    
    press 1 for write messages
    press 2 for inbox
    press 3 for outbox
    press 4 for picture messages
    press 5 for templates
    press 6 for smileys
    press 7 for message settings
    press 8 for info service
    press 9 for voice mailbox number
    press 10 for service command editor
     """
    print(message)
    message_list = int(input("message")
    match message_list:
    
        case 1:
            print("write message")
        case 2:
            print("inbox")
        case 3:
            print("outbox")
        case 4:
            print("picture message")
        case 5:
            print("templates")
        case 6:
            print("smileys")
        case 7:
            print("message settings")
            
            message_setting = """
            press 1 set
            press 2 command
            enter 0 to exist """
            
            match
            message_setting_list:
            case 1
                print("set")
                mesage_Setting = """
                press 1 message center number
                press 2 message sent as
                press 3 message validity
                """
            case 2
                print("command")
                message_setting = """
                press 1 delivery reports
                press 2 reply via same centre
                press 3 character support
    
                """
            case 0: break
            case _:
                print("invalid message")
                
        case 8:
            print("info service")
        case 9:
            print("voice mailbox number")
        case 10:
            print("service command editor")
        case 0: break
        case _:
            print("invalid")
            
        case 3:
            print("chat menu")
        case 4:
            print("call register")
            
            call_register = """
            press 1 for missed calls
            press 2 for recieved calls
            press 3 for dialed numbers
            press 4 for erase recent call list
            press 5 for show call duration
            press 6 for show call costs
            press 7 for call cost settings
            press 8 for prepaid credit
            """
            print(call register)
            call register_list = int(input("call rigester list"))
            match call_register_list:
        case 1:
            print("missed calls")
        case 2:
            print("recieved calls")
        case 3:
            print("dialed numbers")
        case 4:
            print("erase recent call list")
        case 5:
            print("show call duration")
            show_call_duration = """
            press 1 last call duration
            press 2 all calls duration
            press 3 recieved call duration
            press 4 dialed call duration
            press 5 clear timers
            enter 0 to exist
            """
            print(show_call_duration)
            call_duration_list = int(input("show call duration")
                match
            show_call_duration_list:
            case 1:
                print("last call duration")
            case 2:
                print("all call duration")
            case 3:
                print("recieved call duration")
            case 4:
                print("dailed call duration")
            case 5:
                print("clear timers")
            case 0: break
            case _: 
                print("invalid")
        case 6:
            print("show call costs")
            show_call_cost = """
                press 1 last call cost
                press 2 all calls cost
                press 3 clear counters
                enter 0 to exist
                 """
            print(show_call_cost)
            show_call_cost = int(input("show call cost"))
                match
            show_call_cost_list:
            case 1:
                print("last call cost")
            case 2:
                print("all call cost")
            case 3:
                print("clear counter")
            case 0: break
            case _:
                print("invalid")
        case 7:
            print("call cost settings")
            call_cost_setting = """
            press 1 call cost limit
            press 2 show cost in
            enter 0 to exist
            """
            print(call_cost_setting)
            call_cost_setting = int(input("call cost setting"))
                match
            call_cost_setting_list:
            case 1:
                print("call cost limit")
            case 2:
                print("show cost in")
            case 0: break
            case _:
                print("invalid")
        case 8:
            print("prepaid credit")
        case 0: break
        case _:
            print("invalid")
            
        case 5:
        print("tone menu")
        tone_menu = """
        press 1 for ringing tone
        press 2 for ringing volume
        press 3 for incoming call alert
        press 4 for message alert tone
        press 5 for keyboard tones
        press 6 for warning tones
        press 7 for vibrating alert
        press 8 for screen saver
        enter 0 to exist
        """
        print(tone_menu)
        tone_menu_list = int(input("tone menu list"))
            match tone_menu_list:
        case 1:
            print("ringing tone")
        case 2:
            print("ringing volume")
        case 3:
            print("incoming call alert")
        case 4:
            print("message alert tone")
        case 5:
            print("keyboard tones")
        case 6:
            print("warning tones")
        case 7:
            print("vibrating alert")
        case 8:
            print("screen saver")
        case 0: break
        case _:
            print("invalid")
            
        case 6:
            print("setting menu")
            setting_menu = """
        press 1 for call setting
        press 2 for phone setting
        press 3 for security setting
        press 4 for restore setting
        enter 0 to exist
        """
        print(setting_menu)
        settinh_menu_list = int(input("setting menu list")
            match setting_menu_list:
        
        case 1:
            print("call setting")
            call_setting_menu = """
        press 1 for automatic redial
        press 2 for speed dialing
        press 3 for call waiting options
        press 4 for own number sending
        press 5 for phone line in use
        press 6 for automatic answer
        enter 0 to exist
        """
        print(call_setting_menu)
        call_setting_menu_list = int(input("call setting menu")
            match call_setting_menu_list:
            case 1:
                print("automatic redial")
            case 2:
                print("speed dailing")
            case 3:
                print("call waiting options")
            case 4:
                print("own number sending")
            case 5:
                print("phone line in use")
            case 6:
                print("automatic answer")
            case 0: break
            case _:
                print("invalid")
                
        case 2:
            print("phone setting")
            phone_setting_menu ="""
            press 1 for language
            press 2 for cell info display
            press 3 for welcome note
            press 4 for network selection
            press 5 for confirm SIM service actions
            enter 0 to exist
            """
            print(phone_setting_menu)
            phone_setting_menu_list = int(input("phone_setting_menu")
                match phone_setting_menu_list:
            case 1:
                print("language")
            case 2:
                print("cell info display")
            case 3:
                print("welcome note")
            case 4:
                print("network selection")
            case 5:
                print("confirm SIM service actions")
            case 0: break
            case _:
                print("invalid")
                
        case 3:
            print("security setting")
            security_setting_menu = """
            
            press 1 for pin code request
            press 2 for call barring service
            press 3 for fixed dialing
            press 4 for closed user group
            press 5 for security level
            press 6 for change access setting
            enter 0 to exist
            """
            print(security_setting_menu)
            security_setting_menu_list = int(input("security_setting_menu"))
            
                match security_menu_list:
                
            case 1:
                print("pin code request")
            case 2:
                print("call barring service")
            case 3:
                print("fixed dialing")
            case 4:
                print("closed user group")
            case 5:
                print("security level")
            case 6:
                print("change access setting")
            case 0: break
            case _: 
                print("invalid")
        
            case 4:
                print("restore factory setting")
            case 0: break
            case _:
                print("invalid")
                
        case 7:
            print("call divert menu")
        case 8:
            print("music")
            
            music_menu = """
            press 1 for music player
            press 2 for radio
            press 3 for recorder
            press 4 for track list
            enter 0 to exist
            """
            print("music")
            music_menu_list = int(input("music_menu"))
            match clock_menu_list:
            case 1:
                print("music player")
            case 2:
                print("radio")
            case 3:
                print("recorder")
            case 4:
                print("track list")
            case 0: break
            case _:
                print("invalid")
            
        case 9:
            print("games menu")
        case 10:
            print("calculator")
        case 11:
            print("reminders")
        case 12:
            print("clock")
            
            clock_menu = """
            press 1 for alarm clock
            press 2 for clock setting
            press 3 for date setting
            press 4 for stopwatch
            press 5 for countdown timer
            press 6 for auto update of date and time
            enter 0 to exist
            """
            print("clock")
            clock_menu_list = int(input("clocl menu"))
            match clock_menu_list:
            case 1:
                print("alarm clock")
            case 2:
                print("clock setting")
            case 3:
                print("date setting")
            case 4:
                print("stopwatch")
            case 5:
                print("countdown timer")
            case 6:
                print("auto update of date and time")
            case 0: break
            case _:
                print("invalid")
                
        case 13:
            print("profiles")
        case 14:
            print("services")
        case 15:
            print("SIM services")
        case 0:
            break
        case _:
            print("invalid")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
                
            
            
    
            
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
            
            
            
            
    
    
        
            
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        }



