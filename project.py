import pandas as pd
import matplotlib.pyplot as plt
import time
### CSV files
df1=pd.read_csv('User.csv')
df2=pd.read_csv('Podcast.csv')
df3=pd.read_csv('Country.csv')
df4=pd.read_csv('Playlist.csv')
df5=pd.read_csv('Song.csv')
df6=pd.read_csv('Artist.csv')

print(' ',' ~~ ⁕ ~~ '*12)
print(' ',' ~~ ⁕ ~~ '*12)
print('''
                        ███    ███╗ ███████╗██╗      █████╗  ██████╗ ██╗   ██╗  ██╗  ██╗██╗   ██╗██████╗
                        ████  ████║ ██╔════╝██║     ██╔══██╗ ██╔══██╗╚██╗ ██╔╝  ██║  ██║██║   ██║██╔══██╗
                        ██╔████╔██║ █████╗  ██║     ██║  ██║ ██║  ██║ ╚████╔╝   ███████║██║   ██║██████╦╝
                        ██║╚██╔╝██║ ██╔══╝  ██║     ██║  ██║ ██║  ██║  ╚██╔╝    ██╔══██║██║   ██║██╔══██╗
                        ██║ ╚═╝ ██║ ███████╗███████╗╚█████╔╝ ██████╔╝   ██║     ██║  ██║╚██████╔╝██████╦╝
                        ╚═╝     ╚═╝╚══════╝╚══════╝ ╚════╝  ╚═════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
''')
print(' ',' ~~ ⁕ ~~ '*12)
print(' ',' ~~ ⁕ ~~ '*12)
print()
print('''
                                     # # # # # # # # # # # # # # # # # # # # # # # # # # #  
 
                                     #  ░ W ░ h ░ o ░ ░ A ░ r ░ e ░ ░ Y ░ o ░ u ░ ░ ? ░  #

                                     #             1. ░ A ░ D ░ M ░ I ░ N ░              #

                                     #             2. ░ U ░ S ░ E ░ R ░                  #
                                                    
                                     # # # # # # # # # # # # # # # # # # # # # # # # # # #  
''')
ch0=int(input('Enter Your Choice >>> '))

####### ADMIN

if ch0==1:
        
        while True:
                #### MAIN MENU
                
                input('Press ENTER to see main menu...')
                print('''

                        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                                M ♥ E ♥ L ♥ O ♥ D ♥ Y ♥   ♥ H ♥ U ♥ B
                        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                                        
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  
                   |          __  __       _         __  __                          |
                   |         |  \/  |     (_)       |  \/  |                         |
                   |         | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _         |
                   |         | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |        |
                   |         | |  | | (_| | | | | | | |  | |  __/ | | | |_| |        |
                   |         |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|        |
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
                ''')
                print('''
                                        1. Add a new Record 
                                        2. Delete a Record 
                                        3. Modify a Record 
                                        4. Export Dataframe to CSV
                                        5. Exit
                                                                    
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~                                        
                ''')
                ch=int(input('Enter your Choice from Main Menu -----> '))

                ### SELECTION 1
                if ch==1:
                        
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *              In which File do you want to Add a record ?          *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                              ''')
                        ch2= int(input('Enter Your Choice from above Menu -----> '))

                        if ch2==1:## add in users

                                ni= max(df1.index)+1
                                ui=input('Enter User ID: ')
                                un=input('Enter User Name: ')
                                ue=input('Enter Email: ')
                                ps=input('Enter Password: ')
                                rd=input('Enter Registration Date(DD-MM-YYYY): ')
                                gn=input('Enter Gender(Male/Female): ')
                                sb=input('Enter User Subscription(Free/Premium): ')
                                rv=input('Enter Review(in 10 Words or less): ')
                                rt=int(input('Enter Rating (out of 5): '))
                                df1.loc[ni]=[ui,un,ue,ps,rd,gn,sb,rv,rt]
                                df1.to_csv('User.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press ENTER to see Record...')
                                print(df1.loc[[ni]])

                                
                        elif ch2==2:## add in podcast

                                ni= max(df2.index)+1
                                pn=input('Enter Podcast name: ')
                                cr=input('Enter Creator: ')
                                pg=input('Enter Podcast Genre: ')
                                pl=input('Enter Podcast Language: ')
                                ep=int(input('Enter No. of Episodes: '))
                                rt=int(input('Enter Rating(Out of 5): '))
                                df2.loc[ni]=[pn,cr,pg,pl,ep,rt]
                                df2.to_csv('Podcast.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press ENTER to see Record...')
                                print(df2.loc[[ni]])
                                

                        elif ch2==3:## add in country

                                ni= max(df3.index)+1
                                cn= input('Enter Country Name: ')
                                ct= input('Enter Continent Name: ')
                                us= float(input('Enter No of Users(in M): '))
                                pg= input('Enter Popular Genre: ')
                                at= float(input('Enter Avg User Time(in hrs): '))
                                df3.loc[ni]=[cn,ct,us,pg,at]
                                df3.to_csv('Country.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press Enter to see Record...')
                                print(df3.loc[[ni]])
                        
                                
                        elif ch2==4:## add in playlist

                                ni= max(df4.index)+1
                                pi=input('Enter Playlist ID: ')
                                pn=input('Enter Playlist Name: ')
                                cr=input('Enter Creator: ')
                                ns= input("Enter Song ID's: ")
                                vw=float(input('Enter Views(in M): '))
                                dr=float(input('Enter Duration(in hrs): '))
                                df4.loc[ni]=[pi,pn,cr,ns,vw,dr]
                                df4.to_csv('Playlist.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press Enter to see Record...')
                                print(df4.loc[[ni]])
                                           
                                
                        elif ch2==5:## add in song

                                ni= max(df5.index)+1
                                si=input('Enter Song ID: ')
                                tn=input('Enter Track Name: ')
                                an=input('Enter Artist Names: ')
                                ry=int(input('Enter Released Year: '))
                                sp=int(input('Enter in Spotify Playlist: '))
                                st=float(input('Enter no of Streams(in M): '))
                                df5.loc[ni]=[si,tn,an,ry,sp,st]
                                df5.to_csv('Song.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press ENTER to see Record...')
                                print(df5.loc[[ni]])


                        elif ch2==6:## add in artist

                                ni= max(df6.index)+1
                                ai=input('Enter Artist ID: ')
                                an=input('Enter Artist Name: ')
                                nt=input('Enter Artist Nationality: ')
                                rk=int(input('Enter Artist Ranking: '))
                                fl=float(input('Enter Artist Followers(in M): '))
                                ml=float(input('Enter Monthly Listeners(in M): '))
                                df6.loc[ni]=[ai,an,nt,rk,fl,ml]
                                df6.to_csv('Artist.csv',index=False)
                                print('Congrats! Your record has been added')
                                input('Press ENTER to see Record...')
                                print(df6.loc[[ni]])


                        else:
                            print('! Invalid Selection !')

                ### SELECTION 2
                elif ch==2:

                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *           In which File do you want to Delete a record ?          *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                              ''')
                        ch3= int(input('Enter Your Choice from above Menu -----> '))

                        if ch3==1:## del in users
                                print(df1)
                                di=int(input('Enter INDEX to delete: '))
                                df1=pd.read_csv('User.csv')
                                
                                if di in df1.index:
                                        df1.drop(di,axis=0,inplace=True)
                                        df1.to_csv('User.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df1)

                                else:
                                        print('! Index not found !')

                                
                        elif ch3==2:## del in podcast
                                print(df2)
                                di=int(input('Enter INDEX to delete: '))
                                df2=pd.read_csv('Podcast.csv')
                                
                                if di in df2.index:
                                        df2.drop(di,axis=0,inplace=True)
                                        df2.to_csv('Podcast.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df2)

                                else:
                                        print('! Index not found !')

                                
                        elif ch3==3:## del in country
                                print(df3)
                                di=int(input('Enter INDEX to delete: '))
                                df3=pd.read_csv('Country.csv')

                                if di in df3.index:
                                        df3.drop(di,axis=0,inplace=True)
                                        df3.to_csv('Country.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df3)

                                else:
                                        print('! Index not found !')
                                

                                
                        elif ch3==4:## del in playlist
                                print(df4)
                                di=int(input('Enter INDEX to delete: '))
                                df4=pd.read_csv('Playlist.csv')

                                if di in df4.index:
                                        df4.drop(di,axis=0,inplace=True)
                                        df4.to_csv('Playlist.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df4)

                                else:
                                        print('! Index not found !')

                                
                        elif ch3==5:## del in song
                                print(df5)
                                di=int(input('Enter INDEX to delete: '))
                                df5=pd.read_csv('Song.csv')

                                if di in df5.index:
                                        df5.drop(di,axis=0,inplace=True)
                                        df5.to_csv('Song.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df5)

                                else:
                                        print('! Index not found !')

                                
                        elif ch3==6:## del in artist
                                print(df6)
                                di=int(input('Enter INDEX to delete: '))
                                d6=pd.read_csv('Artist.csv')

                                if di in df6.index:
                                        df6.drop(di,axis=0,inplace=True)
                                        df6.to_csv('Artist.csv',index=False)
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df6)

                                else:
                                        print('Your Record has been removed')
                                        input('Press ENTER to see File...')
                                        print(df6)
                                
                        else:
                                print('! Invalid Selection !')

                ### SELECTION 3
                elif ch==3:
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *              In which File do you want to Modify a record ?       *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                              ''')
                        ch4= int(input('Enter Your Choice from above Menu -----> '))

                        if ch4==1:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in USERS ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                                1. User Name
                                                2. User Email
                                                3. Password
                                                4. Subscription
                                                5. Review and Rating
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                ch41=int(input('Enter Your Choice from above Menu -----> '))
                                print(df1)
                                mi= int(input('Enter Index to Modify: '))
                                
                                if ch41==1:
                                        if mi in df1.index:
                                                nun=input('Enter New User Name: ')
                                                df1.loc[mi,'User_Name']=nun
                                                df1.to_csv('User.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df1.loc[[mi],['User_Name']])

                                        else:
                                                print('! Index not Found !')
                                                
                                elif ch41==2:
                                        if mi in df1.index:
                                                nue=input('Enter New User Email: ')
                                                df1.loc[mi,'User_Email']=nue
                                                df1.to_csv('User.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df1.loc[[mi],['User_Email']])

                                        else:
                                                print('! Index not Found !')
                                                
                                elif ch41==3:
                                        if mi in df1.index:
                                                nps=input('Enter New Password: ')
                                                df1.loc[mi,'Password']=nps
                                                df1.to_csv('User.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df1.loc[[mi],['Password']])

                                        else:
                                                print('! Index not Found !')
                                                
                                elif ch41==4:
                                        if mi in df1.index:
                                                nsb=input('Enter Subscription: ')
                                                df1.loc[mi,'Subscription']=nsb
                                                df1.to_csv('User.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df1.loc[[mi],['Subscription']])

                                        else:
                                                print('! Index not Found !')
                                                
                                elif ch41==5:
                                        if mi in df1.index:
                                                nrv=input('Enter New Review: ')
                                                nrt=int(input('Enter New Rating(Out of 5): '))
                                                df1.loc[mi,'Review']=nrv
                                                df1.loc[mi,'Rating']=nrt
                                                df1.to_csv('User.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df1.loc[[mi],['Review','Rating']])

                                        else:
                                                print('! Index not Found !')

                                else:
                                        print('! Invalid Selection !')

                        elif ch4==2:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in PODCAST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                                1. Podcast Name
                                                2. Episodes
                                                3. Rating
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                ch42=int(input('Enter Your Choice from above Menu -----> '))
                                print(df2)
                                mi= int(input('Enter Index to Modify: '))

                                if ch42==1:
                                        if mi in df2.index:
                                                npn=input('Enter New Podcast Name: ')
                                                df2.loc[mi,'Podcast_Name']=npn
                                                df2.to_csv('Podcast.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df2.loc[[mi],['Podcast_Name']])

                                        else:
                                                print('! Index not Found !')

                                elif ch42==2:
                                        if mi in df2.index:
                                                nep=input('Enter Updated Episodes ')
                                                df2.loc[mi,'Episodes']=nep
                                                df2.to_csv('Podcast.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df2.loc[[mi],['Episodes']])

                                        else:
                                                print('! Index not Found !')

                                elif ch42==3:
                                        if mi in df2.index:
                                                nrt=input('Enter New Rating(Out of 5): ')
                                                df2.loc[mi,'Rating']=nrt
                                                df2.to_csv('Podcast.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df2.loc[[mi],['Rating']])

                                        else:
                                                print('! Index not Found !')

                                else:
                                        print('! Invalid Selection !')

                        elif ch4==3:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in COUNTRY ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                                1. No. Of Users
                                                2. Popular Genre
                                                3. Avg User Time
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                ch43=int(input('Enter Your Choice from above Menu -----> '))
                                print(df3)
                                mi= int(input('Enter Index to Modify: '))

                                if ch43==1:
                                        if mi in df3.index:
                                                nnu=input('Enter Updated Users(in M): ')
                                                df3.loc[mi,'Users(in M)']=nnu
                                                df3.to_csv('Country.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df3.loc[[mi],['Users(in M)']])

                                        else:
                                                print('! Index not Found !')

                                elif ch43==2:
                                        if mi in df3.index:
                                                npg=input('Enter New Genre: ')
                                                df3.loc[mi,'Popular_Genre']=npg
                                                df3.to_csv('Country.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df3.loc[[mi],['Popular_Genre']])

                                        else:
                                                print('! Index not Found !')

                                elif ch43==3:
                                        if mi in df3.index:
                                                nat=input('Enter Updated Avg User Time(in hrs): ')
                                                df3.loc[mi,'AvgUserTime(in hrs)']=nat
                                                df3.to_csv('Country.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df3.loc[[mi],['AvgUserTime(in hrs)']])

                                        else:
                                                print('! Index not Found !')

                                else:
                                        print('! Invalid Selection !')

                        elif ch4==4:
                                

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in PLAYLIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. Song ID's
                                              2. Views
                                              3. Duration
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                ch44=int(input('Enter Your Choice from above Menu -----> '))
                                print(df4)
                                mi= int(input('Enter Index to Modify: '))

                                if ch44==1:
                                        if mi in df4.index:
                                                nsi=input("Enter Updated Song ID's: ")
                                                df4.loc[mi,'Song_ID']=nsi
                                                df4.to_csv('Playlist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df4.loc[[mi],['Song_ID']])

                                        else:
                                                print('! Index not Found !')

                                elif ch44==2:
                                        if mi in df4.index:
                                                
                                                nvw=input('Enter Updated Views(in M): ')
                                                df4.loc[mi,'Views (in M)']=nvw
                                                df4.to_csv('Playlist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df4.loc[[mi],['Views (in M)']])

                                        else:
                                                print('! Index not Found !')
                                elif ch44==3:
                                        if mi in df4.index:
                                                ndr=input('Enter New Duration(in hrs): ')
                                                df4.loc[mi,'Duration (in hrs)']=ndr
                                                df4.to_csv('Playlist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df4.loc[[mi],['Duration (in Hr)']])

                                        else:
                                                print('! Index not Found !')
                                else:
                                        print('! Invalid Selection !') 
                                

                        elif ch4==5:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in SONG ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. In Spotify Playlist
                                              2. Streams
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                ch45=int(input('Enter Your Choice from above Menu -----> '))
                                print(df5)
                                mi= int(input('Enter Index to Modify: '))

                                if ch45==1:
                                        if mi in df5.index:
                                                nsp=input('Enter Updated In Spotify Playlist: ')
                                                df5.loc[mi,'in_spotify_playlists ']=nsp
                                                df5.to_csv('Song.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df5.loc[[mi],['in_spotify_playlists ']])

                                        else:
                                                print('! Index not Found !')

                                elif ch45==2:
                                        if mi in df5.index:
                                                nst=input('Enter Updated Streams(in M): ')
                                                df5.loc[mi,'streams(in M)']=nst
                                                df5.to_csv('Song.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df5.loc[[mi],['streams(in M)']])

                                        else:
                                                print('! Index not Found !')

                                else:
                                        print('! Invalid Selection !')

                        elif ch4==6:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     What do you want to Modify in ARTIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. Ranking
                                              2. Followers
                                              3. Monthly Listeners
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                ch46=int(input('Enter Your Choice from above Menu -----> '))
                                print(df6)
                                mi= int(input('Enter Index to Modify: '))

                                if ch46==1:
                                        if mi in df6.index:
                                                nrk=input('Enter New Ranking: ')
                                                df6.loc[mi,'Ranking']=nrk
                                                df6.to_csv('Artist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df6.loc[[mi],['Ranking']])

                                        else:
                                                print('! Index not Found !')
                                elif ch46==2:
                                        
                                        if mi in df6.index:
                                                
                                                nfl=input('Enter Updated Followers(in M): ')
                                                df6.loc[mi,'Followers (in M)']=nfl
                                                df6.to_csv('Artist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df6.loc[[mi],['Followers (in M)']])

                                        else:
                                                print('! Index not Found !')

                                elif ch46==3:
                                        
                                        if mi in df6.index:
                                        
                                                nml=input('Enter Monthly Listeners: ')
                                                df6.loc[mi,'Monthly_Listener(in M)']=nml
                                                df6.to_csv('Artist.csv',index=False)
                                                print('Changes UPDATED')
                                                input('Press ENTER to see Changes...')
                                                print(df6.loc[[mi],['Monthly_Listener(in M)']])

                                        else:
                                                print('! Index not Found !')

                                else:
                                        print('! Invalid Selection !')
                                
                                

                        else:
                                print('! Invalid Selection !')
                                
                                 


                ### SELECTION 4
                elif ch==4:

                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                Which File do you want to export to CSV ?          *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                              ''')
                        ch5=int(input('Enter your Choice from above Menu -----> '))

                        if ch5==1:
                                fn=input('Enter File Name: ')
                                df1.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')
                                
                        elif ch5==2:
                                fn=input('Enter File Name: ')
                                df2.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')
                                
                        elif ch5==3:
                                fn=input('Enter File Name: ')
                                df3.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')
                                
                        elif ch5==4:
                                fn=input('Enter File Name: ')
                                df4.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')
                                
                        elif ch5==5:
                                fn=input('Enter File Name: ')
                                df5.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')
                                
                        elif ch5==6:
                                fn=input('Enter File Name: ')
                                df6.to_csv(fn+'.csv')
                                print('Exporting...')
                                time.sleep(2)
                                print('Congrats! Your file is saved successfully')


                ### SELECTION 5
                elif ch==5:
                        print('')
                        print('''
                                Thank You for choosing 𝓜𝓮𝓵𝓸𝓭𝔂 𝓗𝓾𝓫 :)
                    To know more about us, visit our website " melodyhub.co.in "
                        ''')
                        
                        break

                else:
                        print('! Invalid Selection !')




##### USER
elif ch0==2:
        
        while True:
                #### MAIN MENU
                
                input('Press ENTER to see main menu...')
                print('''

                        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                                M ♥ E ♥ L ♥ O ♥ D ♥ Y ♥   ♥ H ♥ U ♥ B
                        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                                        
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  
                   |          __  __       _         __  __                          |
                   |         |  \/  |     (_)       |  \/  |                         |
                   |         | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _         |
                   |         | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |        |
                   |         | |  | | (_| | | | | | | |  | |  __/ | | | |_| |        |
                   |         |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|        |
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
                ''')
                print('''
                                        1. Read Files
                                        2. Search Records
                                        3. Sort Records
                                        4. Create a Report
                                        5. Data Visualisation
                                        6. EXIT
                                        
                  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~                                        
                ''')
                chm=int(input('Enter your Choice from Main Menu -----> '))

                if chm==1:
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                     Which File do you want to Read ?              *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                           1. Analysis on User                     *
                  *                           2. Analysis on Podcast                  *
                  *                           3. Analysis on Country                  *
                  *                           4. Analysis on Playlist                 *
                  *                           5. Analysis on Songs                    *
                  *                           6. Analysis on Artist                   *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        ''')
                        chm1=int(input('Enter Your Choice from above Menu -----> '))

                        if chm1==1:
                                print(df1)
                        elif chm1==2:
                                print(df2)
                        elif chm1==3:
                                print(df3)
                        elif chm1==4:
                                print(df4)
                        elif chm1==5:
                                print(df5)
                        elif chm1==6:
                               print(df6)
                        else:
                                print('! Invalid Selection !')


                elif chm==2:
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *              In which File do you want to Search a record ?       *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        ''')

                        chm1=int(input('Enter Your Choice from above Menu -----> '))

                        if chm1==1:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in USER ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Registration Date
                                              2. by Gender
                                              3. by Subscription
                                              4. by Ratings
                                              5. User Name
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm11=int(input('Enter Your Choice from above Menu -----> '))

                                if chm11==1:
                                        rd=input('Enter Registration Date(DD-MM-YYYY) to search: ')
                                        cond=df1['Registration_Date']==rd
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df1[cond])

                                elif chm11==2:
                                        gn=input('Enter Gender to search: ')
                                        cond=df1['Gender']==gn
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df1[cond])

                                elif chm11==3:
                                        sb=input('Enter Subscription to search: ')
                                        cond=df1['Subscription']==sb
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df1[cond])

                                elif chm11==4:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Rating ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Rating Above
                                              2. by Rating Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm114=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm114==1:
                                                rt=int(input('Enter Rating(above) to search: '))
                                                cond=df1['Rating']>rt
                                                dfsearch=df1[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df1[cond])
                                        elif chm114==2:
                                                rt=int(input('Enter Rating(below) to search: '))
                                                cond=df1['Rating']<rt
                                                dfsearch=df1[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df1[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm11==5:
                                        un=input('Enter User Name to search: ')
                                        cond=df1['User_Name']==un
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df1[cond])

                                else:
                                        print('! Invalid Selection !')
                                        

                        elif chm1==2:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in PODCAST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Podcast Name
                                              2. by Creator
                                              3. by Genre
                                              4. by Language
                                              5. by Episodes
                                              6. by Ratings
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm12=int(input('Enter Your Choice from above Menu -----> '))

                                if chm12==1:
                                        pn=input('Enter Podcast Name to search: ')
                                        cond=df2['Podcast_Name']==pn
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df2[cond])

                                elif chm12==2:
                                        cr=input('Enter Creator to search: ')
                                        cond=df2['Creator']==cr
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df2[cond])

                                elif chm12==3:
                                        gr=input('Enter Genre to search: ')
                                        cond=df2['Genre']==gr
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df2[cond])

                                elif chm12==4:
                                        lg=input('Enter Language to search: ')
                                        cond=df2['Language']==lg
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df2[cond])

                                elif chm12==5:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Episodes ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Episodes Above
                                              2. by Episodes Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm125=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm125==1:
                                                ep=int(input('Enter Episodes(above) to search: '))
                                                cond=df2['Episodes']>ep
                                                dfsearch=df2[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df2[cond])
                                        elif chm125==2:
                                                ep=int(input('Enter Episodes(below) to search: '))
                                                cond=df2['Episodes']<ep
                                                dfsearch=df2[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df2[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm12==6:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Rating ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Rating Above
                                              2. by Rating Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm126=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm126==1:
                                                rt=float(input('Enter Ratings(above) to search: '))
                                                cond=df2['Rating']>rt
                                                dfsearch=df2[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df2[cond])
                                        elif chm126==2:
                                                rt=float(input('Enter Ratings(below) to search: '))
                                                cond=df2['Rating']<rt
                                                dfsearch=df2[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df2[cond])
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                
                        elif chm1==3:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in COUNTRY ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Country Name
                                              2. by Continent
                                              3. by No. Of Users
                                              4. by Popular Genre
                                              5. by Avg User Time
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm13=int(input('Enter Your Choice from above Menu -----> '))

                                if chm13==1:
                                        cn=input('Enter Country Name to search: ') 
                                        cond=df3['Name']==cn
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df3[cond])

                                elif chm13==2:
                                        ct=input('Enter Continent name to search: ') 
                                        cond=df3['Continent']==ct
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df3[cond])

                                elif chm13==3:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search No of Users ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by No Of Users Above
                                              2. by No Of Users Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm133=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm133==1:
                                                us=float(input('Enter No. Of Users(in M above) to search: ')) 
                                                cond=df3['Users(in M)']>ct 
                                                dfsearch=df3[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df3[cond])
                                        elif chm133==2:
                                                us=float(input('Enter No. Of Users(in M below) to search: ')) 
                                                cond=df3['Users(in M)']<ct 
                                                dfsearch=df3[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df3[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm13==4:
                                        pg= input('Enter Popular Genre to search: ') 
                                        cond=df3['Popular_Genre']==pg 
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df3[cond])

                                elif chm13==5:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Avg Time ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Avg Time Above
                                              2. by Avg Time Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm135=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm135==1:
                                                at= float(input('Enter Average User Time(in hrs above) to search: ')) 
                                                cond=df3['AvgUserTime(in hrs)']>at
                                                dfsearch=df3[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df3[cond])
                                        elif chm135==2:
                                                at= float(input('Enter Average User Time(in hrs below) to search: ')) 
                                                cond=df3['AvgUserTime(in hrs)']<at
                                                dfsearch=df3[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df3[cond])
                                        else:
                                                print('! Invalid Selection !')
                                                

                                else:
                                        print('! Invalid Selection !')



                        elif chm1==4:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in PLAYLIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Playlist ID
                                              2. by Playlist Name
                                              3. by Creator
                                              4. by Song ID's
                                              5. by Views
                                              6. by Duration
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm14=int(input('Enter Your Choice from above Menu -----> '))

                                if chm14==1:
                                        pi=input('Enter Playlist ID to search: ')
                                        cond=df4['Playlist_ID']==pi
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df4[cond])

                                elif chm14==2:
                                        pl=input('Enter Playlist Name to search: ')
                                        cond=df4['Playlist_Name']==pl
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df4[cond])

                                elif chm14==3:
                                        cr=input('Enter Creator to search: ')
                                        cond=df4['Creator']==cr
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df4[cond])

                                elif chm14==4:
                                        si=input("Enter Song ID's(in List) to search: ")
                                        cond=df4['Song_ID']==si
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df4[cond])

                                elif chm14==5:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Views ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Views Above
                                              2. by Views Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm145=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm145==1:
                                                vw=float(input('Enter Views(in M above) to search: '))
                                                cond=df4['Viwes (in M)']>vw
                                                dfsearch=df4[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df4[cond])
                                        elif chm145==2:
                                                vw=float(input('Enter Views(in M below) to search: '))
                                                cond=df4['Views (in M)']<vw
                                                dfsearch=df4[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df4[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm14==6:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Duration ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Duration Above
                                              2. by Duration Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm146=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm146==1:
                                                dr=float(input('Enter Duration(in hrs above) to search: '))
                                                cond=df4['Duration (in hrs)']>dr
                                                dfsearch=df4[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df4[cond])
                                        elif chm146==2:
                                                dr=float(input('Enter Duration(in hrs below) to search: '))
                                                cond=df4['Duration (in hrs)']<dr
                                                dfsearch=df4[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df4[cond])
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')

                        elif chm1==5:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in SONG ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Track Name
                                              2. by Artist(s)
                                              3. by Released Year
                                              4. by Streams
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm15=int(input('Enter Your Choice from above Menu -----> '))

                                if chm15==1:
                                        tn=input('Enter Track Name to search: ')
                                        cond=df5['track_name']==tn
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df5[cond])

                                elif chm15==2:
                                        an=input('Enter Artist(s) to search: ')
                                        cond=df5['artist(s)_name']==an
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df5[cond])

                                elif chm15==3:
                                        ry=int(input('Enter Released Year to search: '))
                                        cond=df5['released_year']==ry
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df5[cond])

                                elif chm15==4:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Streams ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Streams Above
                                              2. by Streams Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm154=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm154==1:
                                                st=int(input('Enter Streams(in M above) to search: '))
                                                cond=df5['streams (in M)']>st
                                                dfsearch=df5[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df5[cond])
                                        elif chm154==2:
                                                st=int(input('Enter Streams(in M below) to search: '))
                                                cond=df5['streams (in M)']<st
                                                dfsearch=df5[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df5[cond])
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')

                        elif chm1==6:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search in ARTIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Artist ID
                                              2. by Artist Name
                                              3. by Nationality
                                              4. by Ranking
                                              5. by Followers
                                              6. by Monthly Listeners
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm16=int(input('Enter Your Choice from above Menu -----> '))

                                if chm16==1:
                                        ai=input('Enter Artist ID to search: ')
                                        cond=df6['Artist_ID']==ai
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df6[cond])

                                elif chm16==2:
                                        an=input('Enter Artist Name to search: ')
                                        cond=df6['Artist_Name']==an
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df6[cond])

                                elif chm16==3:
                                        nt=input('Enter Nationality to search: ')
                                        cond=df6['Nationality']==nt
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')
                                        else:
                                                    print(df6[cond])

                                elif chm16==4:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Ranking ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Ranking Above
                                              2. by Ranking Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm164=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm164==1:
                                                rk=int(input('Enter Ranking(above) to search: '))
                                                cond=df6['Ranking']>rk
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        elif chm164==2:
                                                rk=int(input('Enter Ranking(below) to search: '))
                                                cond=df6['Ranking']<rk
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm16==5:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Followers ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Followers Above
                                              2. by Followers Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm165=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm165==1:
                                                fl=float(input('Enter Followers(in M above) to search: '))
                                                cond=df6['Followers(in M)']>fl
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        elif chm165==2:
                                                fl=float(input('Enter Followers(in M below) to search: '))
                                                cond=df6['Followers(in M)']<fl
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        else:
                                                print('! Invalid Selection !')

                                elif chm16==6:
                                        print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Search Monthly Listeners ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                              1. by Listeners Above
                                              2. by Listeners Below
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        ''')
                                        chm166=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm166==1:
                                                ml=float(input('Enter Monthly Listeners(in M above) to search: '))
                                                cond=df6['Monthly_Listener(in M)']>ml
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        elif chm166==2:
                                                ml=float(input('Enter Monthly Listeners(in M below) to search: '))
                                                cond=df6['Monthly_Listener(in M)']<ml
                                                dfsearch=df6[cond]
                                                if dfsearch.empty:
                                                        print('Not Found')
                                                else:
                                                        print(df6[cond])
                                        else:
                                                print('! Invalid Selection !')
                                                

                                else:
                                        print('! Invalid Selection !')
                                

                        else:
                                print('! Invalid Selection !')



                elif chm==3:
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *              In which File do you want to Sort Records ?          *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        ''')

                        chm2=int(input('Enter Your Choice from above Menu -----> '))

                        if chm2==1:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in USER ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by Registration Date
                                          2. by Rating
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm21=int(input('Enter Your Choice from above Menu -----> '))

                                if chm21==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                 How do you want to sort by Registration Date ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm210=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm210==1:
                                                print(df1.sort_values(['Registration_Date'],ascending=True))
                                        elif chm210==2:
                                                print(df1.sort_values(['Registration_Date'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm21==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                        How do you want to sort by Rating ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm210=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm210==1:
                                                print(df1.sort_values(['Rating'],ascending=True))
                                        elif chm210==2:
                                                print(df1.sort_values(['Rating'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                        

                        elif chm2==2:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in PODCAST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by Episodes
                                          2. by Rating
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm22=int(input('Enter Your Choice from above Menu -----> '))

                                if chm22==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                       How do you want to sort by Episodes ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm220=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm220==1:
                                                print(df2.sort_values(['Episodes'],ascending=True))
                                        elif chm220==2:
                                                print(df2.sort_values(['Episodes'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm22==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                        How do you want to sort by Rating ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm220=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm220==1:
                                                print(df2.sort_values(['Rating'],ascending=True))
                                        elif chm220==2:
                                                print(df2.sort_values(['Rating'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')

                        elif chm2==3:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in COUNTRY ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by Continent
                                          2. by No Of Users
                                          3. by Avg User Time 
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm23=int(input('Enter Your Choice from above Menu -----> '))

                                if chm23==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                      How do you want to sort by Continent ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm230=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm230==1:
                                                print(df3.sort_values(['Continent'],ascending=True))
                                        elif chm230==2:
                                                print(df3.sort_values(['Continent'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm23==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                    How do you want to sort by No of Users ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm230=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm230==1:
                                                print(df3.sort_values(['Users(in M)'],ascending=True))
                                        elif chm230==2:
                                                print(df3.sort_values(['Users(in M)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm23==3:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                   How do you want to sort by Avg User Time ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm230=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm230==1:
                                                print(df3.sort_values(['AvgUserTime(in hrs)'],ascending=True))
                                        elif chm230==2:
                                                print(df3.sort_values(['AvgUserTime(in hrs)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')
                                        
                                else:
                                        print('! Invalid Selection !')
                                        

                        elif chm2==4:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in PLAYLIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by No Of Songs
                                          2. by Views
                                          3. by Duration
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm24=int(input('Enter Your Choice from above Menu -----> '))
                                if chm24==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                   How do you want to sort by No Of Songs ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm240=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm240==1:
                                                print(df4.sort_values(['No_of_Songs'],ascending=True))
                                        elif chm240==2:
                                                print(df4.sort_values(['No_of_Songs'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')
                                                
                                elif chm24==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                      How do you want to sort by Views ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm240=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm240==1:
                                                print(df4.sort_values(['Views (in M)'],ascending=True))
                                        elif chm240==2:
                                                print(df4.sort_values(['Views (in M)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm24==3:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                      How do you want to sort by Duration ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm240=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm240==1:
                                                print(df4.sort_values(['Duration (in hrs)'],ascending=True))
                                        elif chm240==2:
                                                print(df4.sort_values(['Duration (in hrs)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')

                        elif chm2==5:

                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in SONG ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by Released Year
                                          2. by In Spotify Playlists
                                          3. by Streams
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm25=int(input('Enter Your Choice from above Menu -----> '))

                                if chm25==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                   How do you want to sort by Released Year ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm250=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm250==1:
                                                print(df5.sort_values(['released_year'],ascending=True))
                                        elif chm250==2:
                                                print(df5.sort_values(['released_year'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm25==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                How do you want to sort by In Spotify Playlist ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                          1. In Ascending Order
                                          2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm250=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm250==1:
                                                print(df5.sort_values(['in_spotify_playlists '],ascending=True))
                                        elif chm250==2:
                                                print(df5.sort_values(['in_spotify_playlists '],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm25==3:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                    How do you want to sort by Streams ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                            1. In Ascending Order
                                            2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm250=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm250==1:
                                                print(df5.sort_values(['streams (in M))'],ascending=True))
                                        elif chm250==2:
                                                print(df5.sort_values(['streams (in M)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')
                                        
                                else:
                                        print('! Invalid Selection !')

                        elif chm2==6:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                     How do you want to Sort in ARTIST ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                          1. by Ranking
                                          2. by Followers
                                          3. by Monthly Listeners
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm26=int(input('Enter Your Choice from above Menu -----> '))

                                if chm26==1:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                     How do you want to sort by Ranking ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm260=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm260==1:
                                                print(df6.sort_values(['Ranking'],ascending=True))
                                        elif chm260==2:
                                                print(df6.sort_values(['Ranking'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm26==2:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                     How do you want to sort by Followers ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm260=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm260==1:
                                                print(df6.sort_values(['Followers (in M)'],ascending=True))
                                        elif chm260==2:
                                                print(df6.sort_values(['Followers (in M)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                elif chm26==3:
                                        print('''
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                How do you want to sort by Monthly Listeners ?
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                           1. In Ascending Order
                                           2. In Descending Order
                          - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                          ''')
                                        chm260=int(input('Enter Your Choice from above Menu -----> '))
                                        if chm260==1:
                                                print(df6.sort_values(['Monthly_Listener(in M)'],ascending=True))
                                        elif chm260==2:
                                                print(df6.sort_values(['Monthly_Listener(in M)'],ascending=False))
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')


                        else:
                                print('! Invalid Selection !')


                elif chm==4:
                        
                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *              In which File do you want to Create Report ?         *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                              1. Users                             *
                  *                              2. Podcast                           *
                  *                              3. Country                           *
                  *                              4. Playlist                          *
                  *                              5. Songs                             *
                  *                              6. Artist                            *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        ''')

                        chm4=int(input('Enter Your Choice from above Menu -----> '))

                        if chm4==1:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                  How do you want to Create Report in USER ?          
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        1. Users With Subscription                   
                                        2. Users with Rating above                   
                                        3. Users of Gender                           
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm41=int(input('Enter Your Choice from above Menu -----> '))
                                if chm41==1:
                                        sb=input('Enter Subscription to search: ')
                                        cond=df1['Subscription']==sb
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                            print('Not Found')

                                        else:
                                                    print(df1[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm41==2:
                                        rt=int(input('Enter Rating to search: '))
                                        cond=df1['Rating']>rt
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df1[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm41==3:
                                        gn=input('Enter Gender to search: ')
                                        cond=df1['Gender']==gn
                                        dfsearch=df1[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df1[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                                    
                                                        
                
                        elif chm4==2:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                How do you want to Create Report in PODCAST ?        
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        1. Podcast of Genre                           
                                        2. Podcast of Language                        
                                        3. Podcast with Episodes above                
                                        4. Podcast with Ratings above                 
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm42=int(input('Enter Your Choice from above Menu -----> '))
                                if chm42==1:
                                        gr=input('Enter Genre to search: ')
                                        cond=df2['Genre']==gr
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df2[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm42==2:
                                        lg=input('Enter Language to search: ')
                                        cond=df2['Language']==lg
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df2[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm42==3:
                                        ep=int(input('Enter Episodes(above) to search: '))
                                        cond=df2['Episodes']>ep
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df2[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm42==4:
                                        rt=int(input('Enter Genre to search: '))
                                        cond=df2['Genre']>rt
                                        dfsearch=df2[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df2[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                        

                        elif chm4==3:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                               How do you want to Create Report in COUNTRY ?         
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                       1. Country of Continent                       
                                       2. Countries with Users above                 
                                       3. Countries with AvgUserTime above           
                                       4. Countries with Popular Genre               
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm43=int(input('Enter Your Choice from above Menu -----> '))
                                if chm43==1:
                                        ct=input('Enter Continent to search: ')
                                        cond=df3['Continent']==ct
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df3[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm43==2:
                                        ns=float(input('Enter Users(in M above) to search: '))
                                        cond=df3['Users(in M)']>ns
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df3[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm43==3:
                                        at=float(input('Enter AvgUserTime(in M above) to search: '))
                                        cond=df3['AvgUserTime(in hrs)']>at
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df3[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm43==4:
                                        pg=input('Enter Popular Genre to search: ')
                                        cond=df3['Popular_Genre']==pg
                                        dfsearch=df3[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df3[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                

                                
                        elif chm4==4:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                               How do you want to Create Report in PLAYLIST ?         
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                       1. Playlist with No Of Songs above                       
                                       2. Playlist with Views above                 
                                       3. Playlist with Duration above               
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm44=int(input('Enter Your Choice from above Menu -----> '))
                                if chm44==1:
                                        ns=int(input('Enter No Of Songs(above) to search: '))
                                        cond=df4['No_of_Songs']>ns
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df4[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm44==2:
                                        vw=float(input('Enter Views(in M above) to search: '))
                                        cond=df4['Views (in M)']>vw
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df4[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm44==1:
                                        dr=float(input('Enter Duration(in hrs above) to search: '))
                                        cond=df4['Duration (in hrs)']>dr
                                        dfsearch=df4[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df4[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')

                        elif chm4==5:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                               How do you want to Create Report in SONG ?         
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                       1. Songs with Realeased Year                      
                                       2. Songs with In Spotify Playlist above                 
                                       3. Songs with Streams above                
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm45=int(input('Enter Your Choice from above Menu -----> '))
                                if chm45==1:
                                        ry=int(input('Enter Released Year to search: '))
                                        cond=df5['released_year']==ry
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df5[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm45==2:
                                        sp=int(input('Enter In Spotify Playlist(above) to search: '))
                                        cond=df5['in_spotify_playlists ']>sp
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df5[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')
                                

                                elif chm45==3:
                                       
                                        st=float(input('Enter Streams(in M above) to search: '))
                                        cond=df5['streams (in M)']>st
                                        dfsearch=df5[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df5[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !') 

                        elif chm4==6:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                               How do you want to Create Report in ARTIST ?         
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                       1. Artist with Nationality                      
                                       2. Artist with Ranking Above               
                                       3. Artist with Followers above           
                                       4. Artist with Monthly Listeners above               
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                ''')
                                chm46=int(input('Enter Your Choice from above Menu -----> '))
                                if chm46==1:
                                        nt=input('Enter Nationality to search: ')
                                        cond=df6['Nationality']==nt
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df6[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm46==2:
                                        rk=int(input('Enter Ranking(above) to search: '))
                                        cond=df6['Ranking']>rk
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df6[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                
                                elif chm46==3:
                                        fl=float(input('Enter Followers(in M above) to search: '))
                                        cond=df6['Followers (in M)']>fl
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df6[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')

                                elif chm46==3:
                                        ml=float(input('Enter Monthly Listener(in M above) to search: '))
                                        cond=df6['Monthly_Listener(in M)']>ml
                                        dfsearch=df6[cond]
                                        if dfsearch.empty:
                                                    print('Not Found')

                                        else:
                                                    print(df6[cond])
                                                    yn=input('Do you want to save this report(Y/N): ')
                                                    if yn in 'yY':
                                                            fi=input('Enter File Name to save: ')
                                                            dfsearch.to_csv(fi+'.csv')
                                                            print('Saving your report...')
                                                            time.sleep(2)
                                                            print('Congrats! Your file ',fi,' is saved successfully')
                                                    elif yn in 'nN':
                                                            print('Report not saved')

                                                    else:
                                                            print('! Invalid Selection !')
                                else:
                                        print('! Invalid Selection !')
                                
                        else:
                                print('! Invalid Selection !')


                elif chm==5:

                        print('''
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                        DATA VISUALISATION (GRAPHS)                *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                  *                             1. Line Chart                         *
                  *                             2. Bar Graph                          *
                  *                             3. Histogram                          *
                  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        ''')
                        chm5=int(input('Enter Your Choice from above Menu -----> '))

                        if chm5==1:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        Which Line Chart do you want ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        1. Podcast Genre v/s Episodes
                                        2. Country v/s No Of Users
                                        3. Country v/s Avg User Time
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm51=int(input('Enter Your Choice from above Menu -----> '))
                                if chm51==1:
                                        x=df2['Genre']
                                        y=df2['Episodes']
                                        plt.plot(x,y)
                                        plt.xlabel('Genre')
                                        plt.ylabel('Episodes')
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm51==2:
                                        x=df3['Name']
                                        y=df3['Users(in M)']
                                        plt.plot(x,y,label='Users(in M)')
                                        plt.xlabel('Countries')
                                        plt.ylabel('No Of Users(in M)')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm51==3:
                                        x=df3['Name']
                                        y=df3['AvgUserTime(in hrs)']
                                        plt.plot(x,y,label='Avg User Time(in hrs)')
                                        plt.xlabel('Countries')
                                        plt.ylabel('Avg User Time(in hrs)')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')
                                        
                                
                        elif chm5==2:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        Which Bar Graph do you want ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        1. Podcast Language v/s Episodes
                                        2. Podcast Genre v/s Rating
                                        3. Continent v/s No Of Users
                                        4. Songs Released Year v/s Streams
                                        5. Continent v/s No Of Countries
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm52=int(input('Enter Your Choice from above Menu -----> '))
                                if chm52==1:
                                        x=df2['Language']
                                        y=df2['Episodes']
                                        plt.bar(x,y,label='Episodes')
                                        plt.xlabel('Language')
                                        plt.ylabel('No Of Episodes')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm52==2:
                                        x=df2['Genre']
                                        y=df2['Rating']
                                        plt.bar(x,y,label='Rating')
                                        plt.xlabel('Genre')
                                        plt.ylabel('Ratings')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm52==3:
                                        x=df3['Continent']
                                        y=df3['Users(in M)']
                                        plt.bar(x,y,label='Users(in M)')
                                        plt.xlabel('Continents')
                                        plt.ylabel('No Of Users')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm52==4:
                                        x=df5['released_year']
                                        y=df5['streams (in M)']
                                        plt.bar(x,y,label='Streams(in M)')
                                        plt.xlabel('Released Year')
                                        plt.ylabel('No Of Views')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm52==5:
                                        gdf3=df3.groupby('Continent')
                                        gdf31=gdf3.count()
                                        gdf31.plot(kind='bar',y='Name',label='No Of Countries')
                                        plt.legend()
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')
                                        

                                else:
                                        print('! Invalid Selection !')


                        elif chm5==3:
                                print('''
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                        Which Histogram do you want ?
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                                             1. User Rating
                                             2. Podcast Language
                                             3. Podcast Rating
                                             4. Songs Released Year
                  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                              ''')
                                chm53=int(input('Enter Your Choice from above Menu -----> '))
                                if chm53==1:
                                        x=df1['Rating']
                                        plt.hist(x)
                                        plt.xlabel('Ratings')
                                        plt.ylabel('No Of Users')
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm53==2:
                                        x=df2['Language']
                                        plt.hist(x)
                                        plt.xlabel('Language')
                                        plt.ylabel('No Of Podcasts')
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm53==3:
                                        x=df2['Rating']
                                        plt.hist(x,bins=7)
                                        plt.xlabel('Ratings')
                                        plt.ylabel('No Of Podcasts')
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                elif chm53==4:
                                        x=df5['released_year']
                                        plt.hist(x)
                                        plt.xlabel('Released Year')
                                        plt.ylabel('Ratings')
                                        sf=input('Do you want to save the figure ?(Y/N): ')
                                        if sf in 'yY':
                                                fm=input('Enter Graph Name to save: ')
                                                plt.savefig(fm+'.png')
                                                print('Saving your graph...')
                                                time.sleep(2)
                                                plt.show()
                                                print('Congrats! Your Graph is saved successfully')
                                        elif sf in 'nN':
                                                plt.show()
                                        else:
                                                print('! Invalid Selection !')

                                else:
                                        print('! Invalid Selection !')


                        else:
                                print('! Invalid Selection !')
                                


                elif chm==6:
                        print('')
                        print('''
                                Thank You for choosing 𝓜𝓮𝓵𝓸𝓭𝔂 𝓗𝓾𝓫 :)
                    To know more about us, visit our website " melodyhub.co.in "
                        ''')
                        
                        break

                else:
                        print('! Invalid Selection !')
        
else:
    print('! Invalid Selection !')
