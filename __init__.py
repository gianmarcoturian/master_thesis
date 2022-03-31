import random

from otree.api import *
from settings import LANGUAGE_CODE
import random
from pathlib import Path

author = 'Gianmarco Turiano'
doc = """
Experiment
"""


#word list for word game
def load_word_list():
    # words
    return set(Path(__name__ + '/words.txt').read_text().split())

class C(BaseConstants):
    NAME_IN_URL = 'bret'
    PLAYERS_PER_GROUP = None
    RESULTS_1_ROUND_TEMPLATE = __name__ + '/results_1_round.html'
    RESULTS_MULTI_ROUND_TEMPLATE = __name__ + '/results_multi_round.html'
    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Overall Settings and Appearance --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # value of single collected box
    # if the bomb is not collected, player's payoff per round is determined by <box_value> times <boxes_collected>
    # note that the currency of any earnings is determined by the oTree settings in settings.py
    # if you set this to a decimal number, you must set POINTS_DECIMAL_PLACES in settings.py
    BOX_VALUE = cu(1)

    # number of rows and columns
    # i.e. the total number of boxes is determined by <num_rows> times <num_cols>
    NUM_ROWS = 8
    NUM_COLS = 8

    # box height and box width in pixels
    # make sure that the size of the boxes fits the screen of the device
    # note that the layout is responsive, i.e. boxes will break into new rows if they don't fit
    BOX_HEIGHT = '50px'
    BOX_WIDTH = '50px'

    # number of rounds to be played
    NUM_ROUNDS = 1

    # determines whether all rounds played are payed-off or whether one round is randomly chosen for payment
    # if <random_payoff = True>, one round is randomly determined for payment
    # if <random_payoff = False>, the final payoff of the task is the sum of all rounds played
    # note that this is only of interest for the case of <num_rounds> larger than 1
    RANDOM_PAYOFF = True

    # if <instructions = True>, a separate template "Instructions.html" is rendered prior to the task in round 1
    # if <instructions = False>, the task starts immediately (e.g. in case of printed instructions)
    INSTRUCTIONS = True

    # show feedback by resolving boxes, i.e. toggle boxes and show whether bomb was collected or not
    # if <feedback = True>, the button "Solve" will be rendered and active after game play ends ("Stop")
    # if <feedback = False>, the button "Solve" won't be rendered such that no feedback about game outcome is provided
    FEEDBACK = True

    # show results page summarizing the game outcome
    # if <results = True>, a separate page containing all relevant information is displayed after finishing the task
    # if <num_rounds> larger than 1, results are summarized in a table and only shown after all rounds have been played
    RESULTS = True

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Settings Determining Game Play --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # "dynamic" or "static" game play
    # if <dynamic = True>, one box per time interval is collected automatically
    # in case of <dynamic = True>, game play is affected by the variables <time_interval> and <random> below
    # if <dynamic = False>, subjects collect as many boxes as they want by clicking or entering the respective number
    # in case of <dynamic = False>, game play is affected by the variables <random>, <devils_game> and <undoable>
    DYNAMIC = False

    # time interval between single boxes being collected (in seconds)
    # note that this only affects game play if <dynamic = True>
    TIME_INTERVAL = 1.00

    # collect boxes randomly or systematically
    # if <random = False>, boxes are collected row-wise one-by-one, starting in the top-left corner
    # if <random = True>, boxes are collected randomly (Fisher-Yates Algorithm)
    # note that this affects game play in both cases, <dynamic = True> and <dynamic = False>
    RANDOM = False

    # determines whether static game play allows for selecting boxes by clicking or by entering a number
    # if <devils_game = True>, game play is similar to Slovic (1965), i.e. boxes are collected by subjects
    # if <devils_game = False>, subjects enter the number of boxes they want to collect
    # note that this only affects game play if <dynamic = False>
    DEVILS_GAME = True

    # determine whether boxes can be toggled only once or as often as clicked
    # if <undoable = True> boxes can be selected and de-selected indefinitely often
    # if <undoable = False> boxes can be selected only once (i.e. decisions can not be undone)
    # note that this only affects game play if <dynamic = False> and <devils_game = True>
    UNDOABLE = True
    NUM_BOXES = NUM_ROWS * NUM_COLS

    ##word_game
    DIM = 5
    NUM_SQUARES = DIM * DIM
    LEXICON1 = load_word_list()

    COORDS = []

    for x in range(DIM):
        for y in range(DIM):
            COORDS.append((x, y))





from .lexicon_en import Lexicon

which_language = {'en': False, 'de': False}  # noqa
which_language[LANGUAGE_CODE] = True


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)


class Subsession(BaseSubsession):
    pass
##Treatment
def creating_session(subsession: Subsession):
        # randomize to treatments
        import itertools
        randomi=itertools.cycle([True,False])
        for player in subsession.get_players():
            player.positive = next(randomi)
        session = subsession.session
        session.prolific_completion_url = 'https://app.prolific.co/submissions/complete?cc=15B3C407'

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ##welcome
    consent = models.BooleanField(label= 'I have read the above information. I consent to participate in this study.')
    # whether bomb is collected or not
    # store as integer because it's easier for interop with JS
    ####Bomba####
    bomb = models.IntegerField()
    bomb_row = models.IntegerField()
    bomb_col = models.IntegerField()
    boxes_collected = models.IntegerField()
    pay_this_round = models.BooleanField()
    round_result = models.CurrencyField()
    bomb_payoff = models.FloatField()
    ###Investimento####
    investmentA = models.IntegerField(label='How much of your endowment do you invest in the project?', max=100, min=0)
    investmentB = models.IntegerField()
    att_check2 = models.StringField(choices=[['Not Sure', 'Not Sure'], ['Yes', 'Yes'], ['No', 'No']], label='Is the relative likelihood of the two well specified return factors equal in the project?')
    prob_investment = models.IntegerField(label = 'Rate your estimate likelihood that an unspecified outcome occurs. Use a number between 0 to 100, where 0 stands for "it will never happen" and 100 stands for "it will happen for sure".', max=100, min=0)
    hidden_multiplier = models.FloatField()
    randomA = models.FloatField()
    inv_payoff = models.FloatField()
    payoff_tasks = models.FloatField()
    positive = models.BooleanField()
    ###Rischio###
    indifference = models.FloatField(label='Which is the fixed payment in Lottery B that makes you indifferent between the two lotteries?')
    threshold = models.FloatField()
    overthresh = models.BooleanField()
    risk_payoff = models.FloatField()
    att_check1 = models.StringField(choices=[['Not Sure', 'Not Sure'], ['Yes', 'Yes'], ['No', 'No']], label='Should the amount you indicated as fixed payment make you indifferent between Lottery A and Lottery B?')
    prob_risk = models.IntegerField(label = 'Rate your estimate likelihood that an unspecified outcome occurs in Lottery A or B. Use a number between 0 to 100, where 0 stands for "it will never happen" and 100 stands for "it will happen for sure".', max=100, min=0)
    ##Survey###
    ##Big_five###
    unaware = make_q('is willing to face unexpected, unknown, or unforeseen events in general')
    q1 = make_q('is reserved')
    q2 = make_q('is generally trusting')
    q3 = make_q('tends to be lazy')
    q4 = make_q('is relaxed, handles stress well')
    q5 = make_q('has few artistic interests')
    q6 = make_q('is outgoing, sociable')
    q7 = make_q('tends to find fault with others')
    q8 = make_q('does a thorough job')
    q9 = make_q('gets nervous easily')
    q10 = make_q('has an active imagination')
    unawareness = models.IntegerField(label='Rate your willingness to face unexpected, unknown or unforeseen events in general. Use a number between 0 and 10, where 1 stands for completely unwilling and 10 completely willing. ', max=10, min=0)
    extraversion = models.FloatField()
    agreeableness = models.FloatField()
    conscientiousness = models.FloatField()
    neuroticism = models.FloatField()
    openness = models.FloatField()
    ##demografic
    Gender = models.StringField(choices=[['Male', 'Male'], ['Female', 'Female'], ['Prefer not to answer', 'Prefer not to answer']], label='What is your gender?', widget=widgets.RadioSelect)
    Age = models.IntegerField(label='What is your age?')
    Ethnicity = models.StringField(choices=[['White', 'White'], ['Asian', 'Asian'], ['Hispanic', 'Hispanic'], ['Black/African American', 'Black/African American'], ['Other', 'Other']], label='What is your ethnicity background?')
    English = models.StringField(choices=[['Native', 'Native'], ['Fluent', 'Fluent'], ['Basic', 'Basic'], ['Least', 'Least']], label='How fluent are you in English?')
    Education = models.StringField(choices = [['Primary School', 'Primary School'], ['Middle School', 'Middle School'], ['High School','High School'], ['Bachelor or equivalent', 'Bachelor or equivalent'], ['Master/PhD', 'Master/PhD']], label ='What is the highest academic title you achieved?')
    Student = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Are you currently a student?')
    Statistics = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you taken a course in mathematics, statistics, probability or decision making?')
    casino = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Do you often bet real money or play casino-like games?')
    Experiment = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you participated in a lab psychological, behavioral or financial experiment before?')
    Experiment1 = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have you participated in a Prolific/MTurk psychological, behavioral or financial experiment before?')

    student_work = models.StringField(choices=[['Employee', 'Employee'], ['Self-Employed or Company Owner', 'Self-Employed or Company Owner'], ['Manager', 'Manager'],['Does not apply as I am not a student','Does not apply as I am not a student'], ['Other','Other']], blank=True, label='If you are a student, which is the occupation you expected to be in the future?', initial = None)
    workforce = models.StringField(choices=[['Employee', 'Employee'], ['Self-Employed or Company Owner', 'Self-Employed or Company Owner'], ['Manager', 'Manager'],['Homemaker','Homemaker'], ['Unemployed', 'Unemployed'], ['Does not apply as I am a student', 'Does not apply as I am a student'], ['Other','Other']],blank=True, label='If you are not a student anymore, which is your current occupation?', initial = None)
    other = models.StringField(blank = True, label = 'In case you selected "other" in one of the two previous questions, Which is your planned/current occupation? ', initial = None)

    ##Covid
    country = models.StringField(choices = [["AL","Alabama"],["AK","Alaska"],["AZ","Arizona"],["AR","Arkansas"],["CA", "California"],["CO", "Colorado"],
["CT","Connecticut"],["DC","Washington DC"],["DE","Delaware"],["FL","Florida"],["GA","Georgia"],
["HI","Hawaii"],["ID","Idaho"],["IL","Illinois"],["IN","Indiana"],["IA","Iowa"],["KS","Kansas"],["KY","Kentucky"],
["LA","Louisiana"],["ME","Maine"],["MD","Maryland"],["MA","Massachusetts"],["MI","Michigan"],["MN","Minnesota"],
["MS","Mississippi"],["MO","Missouri"],["MT","Montana"],["NE","Nebraska"],["NV","Nevada"],["NH","New Hampshire"],
["NJ","New Jersey"],["NM","New Mexico"],["NY","New York"],["NC","North Carolina"],["ND","North Dakota"],["OH","Ohio"], ["OK","Oklahoma" ],["OR","Oregon"],["PA","Pennsylvania"],["RI","Rhode Island"],["SC","South Carolina"],["SD","South Dakota"],
["TN","Tennessee"],["TX","Texas"],["UT","Utah"],["VT","Vermont"],["VA","Virginia"],["WA","Washington"],["WV","West Virginia"],
["WI","Wisconsin"],["WY","Wyoming"]] , label='Which state are you from?')
    evaluation = models.StringField(choices=[['Not at all affected', 'Not at all affected'], ['Slightly affected', 'Slightly affected'], ['Somewhat affected', 'Somewhat affected'], ['Moderately affected', 'Moderately affected'], ['Extremely affected', 'Extremely affected']], label='Rate how much your state has been affected by Covid-19 pandemic:', widget=widgets.RadioSelect)
    concerned = models.StringField(choices=[['Not at all concerned', 'Not at all concerned'], ['Slightly concerned', 'Slightly concerned'], ['Somewhat concerned', 'Somewhat concerned'], ['Moderately concerned', 'Moderately concerned'], ['Extremely concerned', 'Extremely concerned']], label='Are you concerned about Covid-19 pandemic?', widget=widgets.RadioSelect)
    sintomi = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have any of your relatives experienced symptomatic SarS-CoV-2 infection?')
    hospital = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Have any of your relatives been hospitalized for SarS-CoV-2 infection?')
    death = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Did any of your relatives die for SarS-CoV-2 infection?')
    ###word_game###
    score = models.IntegerField(initial=0)
    board = models.LongStringField()

    ##End##
    fun = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Did you find this experiment fun to play?')
    instruction = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']], label='Were the instructions clear?')
    end = models.StringField(blank=True, label = 'Do you have any suggestion about the experiment that you would like to share? Are there aspects that you think need be improvements? Any suggestion is welcome.')
    finished = models.BooleanField()
# FUNCTIONS

def set_payoff(player: Player):
    participant = player.participant
    round_number = player.round_number

    # determine round_result as (potential) payoff per round
    if player.bomb:
        player.round_result = cu(0)
        player.bomb_payoff = 0
    else:
        player.round_result = player.boxes_collected * C.BOX_VALUE
        player.bomb_payoff = player.boxes_collected
    if round_number == 1:
        participant.vars['round_to_pay'] = random.randint(1, C.NUM_ROUNDS)
    if C.RANDOM_PAYOFF:
        if round_number == participant.vars['round_to_pay']:
            player.pay_this_round = True
            player.payoff = player.round_result
        else:
            player.pay_this_round = False
            player.payoff = cu(0)
    else:
        player.payoff = player.round_result

def combine_score(positive, negative):
    return 3 + (positive - negative) / 2

class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']
    @staticmethod
    def error_message(player, values):
        if values['consent'] != True :
            return 'You should accept the consent form to proceed to the experiment'
class Instructions_Bomb(Page):
    @staticmethod
    def is_displayed(player: Player):
        return C.INSTRUCTIONS and player.round_number == 1

   # @staticmethod
   # def vars_for_template(player: Player):
       # return dict(num_nobomb=C.NUM_BOXES - 1)


class Bomb(Page):
    # form fields on player level
    form_model = 'player'
    form_fields = [
        'bomb',
        'boxes_collected',
        'bomb_row',
        'bomb_col',
    ]

   # @staticmethod
    #def vars_for_template(player: Player):
        #return dict(Lexicon=Lexicon)

    @staticmethod
    def js_vars(player: Player):
        participant = player.participant
        reset = participant.vars.pop('reset', False)
        if C.DYNAMIC:
            show_input = False
        else:
            show_input = not C.DEVILS_GAME
        return dict(
            reset=reset,
            show_input=show_input,
            NUM_ROWS=C.NUM_ROWS,
            NUM_COLS=C.NUM_COLS,
            BOX_HEIGHT=C.BOX_HEIGHT,
            BOX_WIDTH=C.BOX_WIDTH,
            FEEDBACK=C.FEEDBACK,
            RESULTS=C.RESULTS,
            DYNAMIC=C.DYNAMIC,
            TIME_INTERVAL=C.TIME_INTERVAL,
            RANDOM=C.RANDOM,
            UNDOABLE=C.UNDOABLE,
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['reset'] = True
        set_payoff(player)

    @staticmethod
    def error_message(player, values):
            if values['boxes_collected'] == 0 :
                return 'Please, play the game.'

class Investimento(Page):
    form_model = 'player'
    form_fields = ['investmentA', 'prob_investment', 'att_check2']
    @staticmethod
    def before_next_page(player: Player,timeout_happened):
        import random
        possibility = [0, 0.4, 1, 1.5, 2, 2.5]
        h_mult = random.choice(possibility)
        player.hidden_multiplier = h_mult
        weight_A = [0.5,3,h_mult]
        drawn_A = random.choice(weight_A)
        player.randomA = drawn_A
        player.investmentB = 100 - player.investmentA
        payoff = player.investmentA * drawn_A + player.investmentB
        player.inv_payoff = payoff
        player.payoff_tasks = player.inv_payoff + player.risk_payoff + player.bomb_payoff
    @staticmethod
    def error_message(player, values):
        if values['att_check2'] != 'Yes':
            return 'Please, read carefully the instructions'

class Rischio(Page):
    form_model = 'player'
    form_fields = ['indifference', 'prob_risk', 'att_check1']
    @staticmethod
    def before_next_page(player: Player,timeout_happened):
        import random
        outcome_A = [0, 40, 70, 100, 125]
        weightsA = [3, 2, 5, 1, 2]
        outcome_B = [ 40, 70, 100, player.indifference]
        weightsB = [2, 5, 1, 5]
        threshold = random.randrange(0,100)
        player.threshold = threshold
        if player.indifference < threshold :
            player.overthresh = False
            B_happ = random.choices(outcome_B, weights = weightsB, k=1)
            payoff = float(B_happ[0])
        else:
            player.overthresh = True
            A_happ = random.choices(outcome_A, weights = weightsA, k=1)
            payoff = float(A_happ[0])
        player.risk_payoff = payoff

    @staticmethod
    def error_message(player, values):
        if values['att_check1'] != 'Yes':
            return 'Please, read carefully the instructions'


class Results_Bomb(Page):
    @staticmethod
    def is_displayed(player: Player):
        return C.RESULTS and player.round_number == C.NUM_ROUNDS

    # @staticmethod
    # def vars_for_template(player: Player):
        # participant = player.participant
        # total_payoff = sum([p.payoff for p in player.in_all_rounds()])
        # participant.vars['bret_payoff'] = total_payoff
        # return dict(
           # player_in_all_rounds=player.in_all_rounds(),
            # box_value=C.BOX_VALUE,
            # boxes_collected=player.boxes_collected,
            # bomb=player.bomb,
            # bomb_row=player.bomb_row,
            # bomb_col=player.bomb_col,
            # round_result=player.round_result,
            # round_to_pay=participant.vars['round_to_pay'],
            # payoff=player.payoff,
            # total_payoff=total_payoff,
       # )

class Results_investimento(Page):
    form_model = 'player'
class Results_rischio(Page):
    form_model = 'player'

###Survey###

class Instruction_survey(Page):
    form_model = 'player'
class BigFive_riserve(Page):
    form_model = 'player'
    form_fields = ['unawareness', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.extraversion = combine_score(player.q6, player.q1)
        player.agreeableness = combine_score(player.q2, player.q7)
        player.conscientiousness = combine_score(player.q8, player.q3)
        player.neuroticism = combine_score(player.q9, player.q4)
        player.openness = combine_score(player.q10, player.q5)
class Demographics(Page):
    form_model = 'player'
    form_fields = ['Gender', 'Age', 'Ethnicity', 'English','Education', 'Student', 'student_work', 'workforce','other', 'Statistics', 'casino', 'Experiment','Experiment1']

    @staticmethod
    def error_message(player, values):
        if values['Student'] == True:
            if values['workforce'] != 'Does not apply as I am a student':
                if values['workforce'] !=  '' :
                    return 'Your answers are not consistent. Please, check them.'
            if values ['student_work'] == '' or values['student_work'] == 'Does not apply as I am not a student' :
                 return 'Your answers are not consistent. Please, check them.'
        if values['Student'] != True:
            if values['student_work'] != 'Does not apply as I am not a student':
                if values['student_work'] !=  '' :
                    return 'Your answers are not consistent. Please, check them.'
            if values ['workforce'] == '' or values['workforce'] == 'Does not apply as I am a student' :
                 return 'Your answers are not consistent. Please, check them.'

        if values['student_work'] != 'Other' and values['workforce'] != 'Other' :
            if values['other'] != '':
                return 'Your answers are not consistent. Please, check them.'
        if values['student_work'] == 'Other' or values['workforce'] == 'Other' :
            if values['other'] == '' :
                return 'Your answers are not consistent. Please, check them.'


class Covid(Page):
    form_model = 'player'
    form_fields = ['country', 'evaluation', 'concerned', 'sintomi', 'hospital', 'death']

##Word_game###

class FoundWord(ExtraModel):
    word = models.StringField()
    player = models.Link(Player)

def word_in_board(word, board):
    lengths = list(range(1, len(word) + 1))
    paths = {_: [] for _ in lengths}

    for i in range(C.DIM):
        for j in range(C.DIM):
            coord = (i, j)
            if board[coord] == word[0]:
                paths[1].append([coord])

    for length in lengths[1:]:
        target_char = word[length - 1]
        for path in paths[length - 1]:
            cur_x, cur_y = path[-1]
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    check_coord = (cur_x + dx, cur_y + dy)
                    if (
                        check_coord in C.COORDS
                        and board[check_coord] == target_char
                        and check_coord not in path
                    ):
                        paths[length].append(path + [check_coord])
    return bool(paths[len(word)])


def load_board(board_str):
    return dict(zip(C.COORDS, board_str.replace('\n', '').lower()))

class Instructions_word(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        rows = []
        for _ in range(C.DIM):
            # add extra vowels
            row = ''.join(
                [random.choice('AAABCDEEEEEFGHIIKLMNNOOPRRSTTUUVWXYZ') for _ in range(C.DIM)]
            )
            rows.append(row)
        player.board = '\n'.join(rows)



def live_method(player: Player, data):
    board = player.board

    if 'word' in data:
        word = data['word'].lower()
        is_in_board = len(word) >= 3 and word_in_board(word, load_board(board))
        is_in_lexicon = is_in_board and word.lower() in C.LEXICON1
        is_valid = is_in_board and is_in_lexicon
        already_found = is_valid and bool(FoundWord.filter(player=player, word=word))
        success = is_valid and not already_found
        news = dict(
            word=word,
            success=success,
            is_in_board=is_in_board,
            is_in_lexicon=is_in_lexicon,
            already_found=already_found,
            id_in_group=player.id_in_group,
        )
        if success:
            FoundWord.create(player=player, word=word)
            player.score += 5
    else:
        news = {}
    scores = [[player.id_in_group, player.score]]
    found_words = [fw.word for fw in FoundWord.filter(player=player)]
    return {0: dict(news=news, scores=scores, found_words=found_words)}


class word_game(Page):
    live_method = live_method
    timeout_seconds = 3* 60

    @staticmethod
    def vars_for_template(player: Player):
        return dict(board=player.board.upper().split('\n'))

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.payoff = player.score + player.bomb_payoff + player.inv_payoff + player.risk_payoff

class Results_word(Page):
    form_model = 'player'
class Results_total(Page):
    form_model = 'player'
class Final (Page):
    form_model = 'player'
    form_fields = ['fun', 'instruction', 'end']
    @staticmethod
    def before_next_page(player:Player, timeout_happened):
        participant = player.participant
        player.finished = True
        participant.finished = True

class Exit (Page):
    pass

page_sequence = [Welcome, Instructions_Bomb, Bomb, Rischio, Investimento, Instruction_survey, BigFive_riserve, Demographics, Covid, Instructions_word, word_game,  Results_Bomb, Results_rischio, Results_investimento, Results_word, Final, Exit]
