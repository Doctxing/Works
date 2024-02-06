# Coded by iXterior

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
import math

class Alpha:  

    def __init__(self,ifplt=1):
        self.ifplt=ifplt
    def fit(self,X_train,Y_train) -> None:
        pass
    def predict(self,X_test:pd):
        Y_pre = np.zeros(X_test.shape[0])
        for i in range(0,1):
            Y_pre[i] = X_test.loc[i,'DELM']
            
        for k in range(1,X_test.shape[0]):
            H=[-1.8851000000000013,-1.8594000000000008,-1.8594000000000008,-1.859399999999999,-1.8483406020957522,-1.7896,-1.7896,-1.7896,-1.7895999999999983,-1.7895999999999983,-1.7895999999999965,-1.7895999999999965,-1.7709406859988266,-1.7654809062747954,-1.755898932059789,-1.7094000000000023,-1.6598948159452322,-1.6396000000000015,-1.6395999999999997,-1.6001155187246727,-1.6000000000000032,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.6000000000000014,-1.5999999999999979,-1.5999999999999979,-1.5999999999999979,-1.5807266127781956,-1.5759903450665895,-1.5683411815133574,-1.5653626223966484,-1.5500411915452448,-1.4961710102720471,-1.4500000000000028,-1.4499999999999993,-1.4499999999999993,-1.4499999999999993,-1.4484009776532076,-0.8351000000000006,-0.7799062456110479,-0.7396000000000011,-0.7395999999999958,-0.7395999999999958,-0.7224059498223143,-0.7048111423889885,-0.6850999999999985,-0.6850999999999985,-0.659399999999998,-0.5896000000000008,-0.5895999999999972,-0.5895999999999972,-0.5500000000000043,-0.5499999999999989,-0.5499999999999972,-0.546777635574903,-0.47731242647081196,-0.40000000000000036,-0.3999999999999986,-0.3999999999999986,-0.3999999999999986,-0.3999999999999915,-0.3913178558508714,-0.3868004657228581,0.0,0.3999999999999986,0.3999999999999986,0.3999999999999986,0.39999999999999947,0.40000000000000213,0.4388933306176308,0.5004850266453049,0.5499999999999972,0.5895999999999999,0.6510522521591362,0.6593999999999944,0.659399999999998,0.6594000000000015,0.6671387519721801,0.6944999999999979,0.6945000000000014,0.698000000000004,0.7279447686737539,0.7395999999999887,0.7562407762858303,0.8093999999999966,0.8094000000000001,0.8351000000000006,0.8351000000000042,0.8445,0.8445000000000018,1.4480483415463086,1.4499999999999957,1.4499999999999957,1.4499999999999993,1.4499999999999993,1.4499999999999993,1.4500000000000028,1.4500000000000028,1.4500000000000028,1.4500000000000028,1.4647559970937913,1.54866712671492,1.5841982544512705,1.5982672191299008,1.5999999999999996,1.5999999999999996,1.5999999999999996,1.5999999999999996,1.5999999999999996,1.6000000000000014,1.6000000000000014,1.6000000000000014,1.6000000000000014,1.6000000000000014,1.605009864691095,1.6204468142671709,1.6337928749266593,1.6395999999999944,1.639599999999998,1.6395999999999997,1.6396000000000015,1.6396000000000015,1.6396000000000015,1.6451191818842323,1.7093999999999987,1.7094000000000023,1.720465083249481,1.7273212715571624,1.748000000000001,1.7493000000000016,1.7620457441989839,1.7896,1.7896,1.7896,1.7896,1.7896,1.7896000000000036,1.7896000000000036,1.8018337670352125,1.857010710105759,1.8594000000000008,1.8594000000000008,1.8594000000000008,1.8709579524002047,1.871596345352347,1.8851000000000013,1.8851000000000013,1.8851000000000013,1.8851000000000013,1.890973215159705,1.8945000000000007,1.8979999999999997,1.8992999999999984,]
            df = X_test.iloc[:k+1,:]
            df['G'] = 0.
            for i in range(k,df.shape[0]):
                df.loc[i,'G'] = df.loc[i,'DELM'] - df.loc[i-1,'DELM']
            #df.dropna().reset_index(drop=True)

            # P(模拟概率值的建模，P越靠近0.5说明预测为逆风局边缘，双方差距不大，靠近0——1优势，靠近1——2优势)
            P = np.zeros(df.shape[0]) 
            for i in range(k,df.shape[0]):
                n = 0
                if i==0:
                    P[i] = 0.01
                    continue
                for j in range(len(H)):
                    if df.loc[i,'G'] > H[j]:
                        n+=1
                    else:
                        pass
                P[i] = (n/len(H))
            # print(P)

            def dimensionlessProcessing(nparr:np.array,X):
                MAX  = np.max(X)
                MIN  = np.min(X)
                MEAN = np.mean(X)
                return ((nparr - MEAN) / (MAX - MIN))

            # Score 上一轮的两者单game的分数差
            Score = np.array([df.loc[i,'p1_score'] - df.loc[i,'p2_score'] for i in range(0,df.shape[0])])
            #Score = dimensionlessProcessing(Score,X_test.loc[:,'p1_score'].values-X_test.loc[:,'p2_score'].values)
            # print(Score)

            # Server
            Server = -(df.loc[:,'server'].values * 2 - 3)
            #Server = dimensionlessProcessing(Server)
            # print(Server)

            # G 上一轮的 G 值 对 这一轮的概率有何影响
            G = np.zeros(df.shape[0])
            for i in range(k,df.shape[0]):
                G[i] = df.loc[i-1,'G']
            #G = dimensionlessProcessing(G,H)
            # print(G)

            # Bp 赛点
            Bp = df.loc[:,'p1_break_pt'].values - df.loc[:,'p2_break_pt'].values
            #Bp = dimensionlessProcessing(Bp,X_test.loc[:,'p1_break_pt'].values - X_test.loc[:,'p2_break_pt'].values)
            # print(Bp)

            # R 两者跑动距离之差
            R = df.loc[:,'1runsum'].values - df.loc[:,'2runsum'].values
            #R = dimensionlessProcessing(P,[0,0.5,1])
            # print(R)

            # V 球速
            V = df.loc[:,'speed_mph'].values
            V = dimensionlessProcessing(V,X_test.loc[:,'speed_mph'].values)
            # print(V)

            # S_wdh 发球者
            S_wdh = df.loc[:,'serve_width'].values
            s0 = np.zeros(df.shape[0])
            s1 = np.zeros(df.shape[0])
            s2 = np.zeros(df.shape[0])
            s3 = np.zeros(df.shape[0])
            s4 = np.zeros(df.shape[0])

            for i in range(k,df.shape[0]):
                if S_wdh[i] == 0:
                    s0[i] = 1
                elif S_wdh[i] == 1:
                    s1[i] = 1
                elif S_wdh[i] == 2:
                    s2[i] = 1
                elif S_wdh[i] == 3:
                    s3[i] = 1
                else:
                    s4[i] = 1

            #S_wdh = dimensionlessProcessing(S_wdh)
            #print(S_wdh)

            # S_dph 发球者
            S_dph = df.loc[:,'serve_depth'].values
            #S_dph = dimensionlessProcessing(S_dph)
            # print(S_dph)

            # R_dph 接求者
            R_dph = df.loc[:,'serve_depth'].values
            #R_dph = dimensionlessProcessing(R_dph)
            # print(R_dph)

            # Net 
            Net = df.loc[:,'p1_net_pt'].values - df.loc[:,'p2_net_pt'].values
            #Net = dimensionlessProcessing(Net)
            # print(Net)
            a0 = 0.02487295261707338
            delta = [
            -1.341425334629614,1.34913551024473,1.410475256696752,0.2660694571982221,0.7696471774539705,
            -0.5336554865137383,-0.03104444895136851,1.696191360533341,-0.05078481909718342,1.26868652422087,
            0.5410885280489712,0.1318157526841554,1.188702103343439,0.7960218101097388,-0.5781844508181735,
            -1.629594885533915,0.9148007648294862,-1.006579719310543,-1.020210870165751,1.337903835083826,
            0.005068855399505733,-0.3590675655980871,0.1239662773447658,-0.8049525061483414,-0.2134830337333848,
            -0.4067358805514706,-0.1480810617685772,-0.7367692569014747,1.099818456014218,1.051657365865893,
            0.1241428900807405,0.009996808596981002,-1.157189447373317,0.8807817808092941,0.6103753580758797,
            -1.075657673449573,0.646871481439016,-1.121134097680253,0.5883753150915084,-0.2035703138851746,
            -0.6181034919417384,-1.355014758373551,-1.372644593082003,-0.9685846181223593,1.544454564727532,
            0.4936985100238371,-0.6613825308806169,-0.2280530458070724,-0.9616992625213715,0.8986081415867732,
            0.03646996278560445,-0.872539175629209,-1.927979372230165,0.2567662419226468,-1.244342722713624,
            -0.8287440452767248,-1.498580854853458,-0.2957073435184345,0.6399737673372244,-0.1097561854774844,
            0.7363535981954041,0.6636352942553582,0.3461465790462088,0.2966587593221779,0.7305223347818157,
            1.115084583130431,0.2083792535863238,0.2561938060221612,-0.3413975984400995,-1.167054413989218,
            0.677585060237497,1.16832630735838,-0.8844676584574158,1.851259730456774,-1.440544919057451,
            -0.4109632705977151,-0.2917466497532389,0.5267122766981683,-1.146005905402342,0.8398562947467355,
            -0.1840350658946011,-0.4946982112188669,-0.9439828952864471,-0.8385686129022996,0.9312059198247541,
            -0.1605048456358695,0.1326745125454637,-0.5180611269154064,-0.1379178165112087,-1.211719377967254,
            -0.1574746689716172,0.3219564405113884,-0.6206504461476184,0.07066595176065674,0.9109095670025861,
            -0.4329864238404617,-0.1322087661711904,-1.019223277527797,-1.114239650844904,0.4445851524553797,
            1.727964590844978,0.203170800088207,0.9914648853345724,0.4723447447452221,-0.05111549851636921,
            1.336172015940112,0.289231396802928,-0.7383900857704279,-1.109281396135097,0.2676227540818958,
            -0.8961109720240956,0.3650254775140141,-0.09554036988097349,0.4054083441183322,0.667449159322264,
            0.04174175726872754,-0.1288052848737789,-0.8892960993937143,1.453712861349158,0.5218846134633258,
            -0.07528438058052407,0.4126794145113568,-0.8119577253672867,1.645801412982166,-0.848200025773904,
            0.2649724666007843,0.3842285029535302,0.9207542021885138,0.4141743260681218,0.6269662974595818,
            -0.272188829757159,1.165064913152947,-0.06884710749867355,0.3307114156370787,-0.7738441500556424,
            -1.390038464745269,0.4170196366530545,0.196789048037965,-0.3404397947557473,0.05924604609969856,
            -1.393459508009377,0.2426533790306466,0.1781662832133004,0.3652803517358723,0.2935151204879256,
            -0.3235432345708728,0.3194782768659561,1.937313095628131,-1.316844343350629,-0.5184790113341706,
            0.5840495184587665,0.220653938674205,-1.40790328816027,0.4611159703173074,0.2759973975005408,
            -0.4866727052324309,0.1918039237306148,-1.076264019474968,-0.1993337060716026,-0.3282209128207569,
            -0.9519584050891736,0.6239116374502084,-1.16250253790128,-0.37104013492626,-0.4806715282676537,
            0.4740775006144453,-0.5938453336416682,-0.7468139885979801,0.5663314832611104,0.9838902030213345,
            0.5841716452432447,1.22517099076391,-0.1177567347872526,0.2926596560745395,0.8629291830745415,
            -0.7913017573358517,-1.120241781608923,-0.5315064098698933,-0.4575974619040541,0.7105287770278451,
            0.2849391899700957,-1.232548096543846,0.3453566089519109,0.04103646032144225,0.6948153083576212,
            -1.135463426942081,-0.6995732778725839,-1.130126019215473,1.933987324005378,0.2739191431300951,
            -0.5106441772472635,0.07566987441886878,-1.29063185942554,0.8023281016132379,0.04536261288479916,
            -0.1598577412199755,-0.9677862584185981,-0.1779486806420843,-0.5936079079321777,-0.5974385148750483,
            -0.1172866115862289,-0.142836329316874,0.1894572532352537,-1.174054738812358,-0.3308959795715805,
            1.242286860144871,0.7783754012396608,0.656867516600775,-0.7852169182981501,-0.2999222517952232,
            -0.7187971915153327,0.1746067875765087,-0.2572610183725591,-0.541331929453577,0.2531643791403048,
            0.2385905930400905,1.794321548793688,-0.8118420738624578,0.5667613722040633,0.9305309862773277,
            0.002351291121398426,0.2776028887251388,0.07429200840024784,0.3616449117366186,-0.328879736989996,
            0.2157963741330371,0.7523942431148839,-1.193922115740677,-0.6468902922495623,1.121365468141285,
            -1.825476452972109,0.5699555352460055,1.534031604613995,-0.3290898122821162,1.302824602763335,
            -0.04252028413765939,-1.046724229758581,0.3521999770262241,0.14807991984751,-0.2677604781705834,
            1.079532483573168,-2.586088498786364,0.7278837035308924,-0.1144770873941012,-0.2391892668490483,
            -0.3453539911550905,-1.922187951238914,0.5518155026455226,0.2931890656833076,0.462754876789401,
            0.09206472200931388,1.103584463584262,0.3170539435831788,0.6937816035120672,1.257734949286189,
            -1.372679799733942,0.2737959578792291,0.7914619325735722,-0.06996021763210532,0.4488393461816889,
            -0.3592520176093297,-0.06026829625394599,0.9161093146780795,0.2831484496199532,0.649440430979908,
            0.827241952751814,0.6427787003925345,0.03402236941770685,-0.688355483537427,0.2511017086794497,
            -0.8900130392719655,0.1624228647055677,1.11861027680412,0.9279816595211989,-0.3436642945995125,
            1.12252783806121,0.7695943104786674,-0.7565542696032634,0.8930842102372417,0.1797916177019109,
            -0.571382313669341,-0.9726933610250112,1.27802567055137,1.135648945710877,-0.184432073923341,
            -0.4747293995519874,-0.5218228227081401,-0.1373409202478675,1.114548658803711,-0.2571427774306474,
            0.4296031089356509,-0.9694685159730474,-0.4090780262757009,0.3478860628824599,-0.1594032824136621,
            0.9006967045333165,0.1588641446169639,-0.1292153974975588,-0.8455984192625722,0.9710529759819022,
            -0.8758933581458561,-0.220618308774058,-0.4330075746901217,0.7553869960577552,-0.1732940186306136,
            -0.680017203753797,-0.395039846611507,-0.5799345472837445,-0.666795371038419,0.2652084639925431,
            -0.3111832972406878,-0.03601670626406841,0.8230948982736599,1.141711931986372,-0.5036549633131538,
            0.1814329604141066,0.02039840444568691,1.110823104492927,0.7096324734175932,-0.3300355791735359,
            -0.3603415917339533]
            g0 = 0.1989525110900083
            g1 = 0.01217439055417175
            g2 = -0.001054595497499601
            g3 = -2.210053123817004
            g4 = -0.07406493436431361
            g5 = -0.7027931268581541
            g6 = -7.449886088627544
            g7 = 0.03303518626734488
            k0 = 7.268723615007642
            k1 = 7.877432318024248
            k2 = 7.982807803513984
            k3 = 8.640302697956583
            k4 = 8.683567710079924
            k5 = -6.715647459639007
            k6 = 6.16637593236711
            tau = 35.97649715984348
            tau_d = 1.562316130156271
            
            def obj(i,r=[s0[i],s1[i],s2[i],s3[i],s4[i],S_dph[i],R_dph[i]]):
                Ss = r[0]*k0 + r[1]*k1 + r[2]*k2 + r[3]*k3 + r[4]*k4 + r[5]*k5 + r[6]*k6
                Gs = g0*G[i]  + g1*Score[i] + g2*R[i] +g3*V[i] + g4*Net[i]+ g5*Bp[i] + g6*Server[i] + g7*Server[i]*G[i]
                t = a0 + Ss*Server[i] + Gs + delta[int(i/df.shape[0]*321)]
                #return t
                return 1/(1+np.exp(-t))
            #delta[int(i/df.shape[0]*320)]

            pre = np.zeros(df.shape[0])
            '''max  = np.max(df.loc[:,'G'].values)
            min  = np.min(df.loc[:,'G'].values)
            print(df.loc[:,'G'].values)
            print(max,min)'''
            for i in range(k,df.shape[0]):
                pre[i] = obj(i)
                print(pre[i])
                m = pre[i]
                if m>=1:
                    m=1
                if m<=0:
                    m=0
                pre[i] = H[int(m*len(H))-1]
                #pre[i] = m
            Y_pre[k] = X_test.loc[k-1,'DELM'] + pre[k]
            #Y_pre[k] = X_test.loc[k-1,'DELM'] + df.loc[k,'G']
            '''if k==X_test.shape[0]-1:
                #pre[k] = pre[k]*(max-min)+min
                sns.lineplot(pre)
                sns.lineplot(df.loc[:,'G'])
                #sns.lineplot(pre-df.loc[:,'G'])
                plt.show()
                print(df.loc[k,'G'])
                print(X_test.loc[k-1,'DELM'])
            print(Y_pre[k])     '''
        if self.ifplt==1:
            sns.lineplot(Y_pre)
            sns.lineplot(X_test.loc[:,'DELM'].values)
            print(X_test.loc[X_test.shape[0]-1,'DELM'])
            plt.show()
        return Y_pre
                

if __name__ == '__main__':
    df = pd.read_csv('./data/processed/processed1305.csv')
    Alpha().predict(df)