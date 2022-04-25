from experta import *
import ast


class MedicalExpert(KnowledgeEngine):
    username = "", 


    @DefFacts()
    def needed_data(self):
        """ 
        This is a method which is called everytime engine.reset() is called.
        It acts like a constructor to this class.
        """        
        yield Fact(findDisease = 'true')
        print("Hi! I am Mr.Expert.\n\nYou can get yourself diagnosed here free of cost!\nI will ask you 10 questions.\n\n")

    Rule(Fact(findDisease = 'true'),NOT(Fact(name=W())),salience = 1000)
    def ask_name(self):
        self.username = input("What's your name?\n")
        self.declare(Fact(name=self.username))

    @Rule(Fact(findDisease='true'), NOT (Fact(chestPain = W())),salience = 995)
    def hasChestPain(self):
        self.chest_pain = input("\nDo you have chest pain?\nPlease type Yes/No\n")
        self.chest_pain = self.chest_pain.lower()
        self.declare(Fact(chestPain = self.chest_pain.strip().lower()))

    # @Rule(Fact(findDisease='true'), (Fact(chestPain = 'yes')),salience = 990)
    # def hasSevereChestPain(self):
    #     self.severe_chest_pain = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_chest_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        self.cough = input("\nDo you have cough?\nPlease type Yes/No\n")
        self.cough = self.cough.lower()
        self.declare(Fact(cough = self.cough.strip().lower()))

    #rrrrrrrrrrrrr
    # @Rule(Fact(findDisease='true'), (Fact(cough = 'yes')),salience = 980)
    # def hasSevereCough(self):
    #     self.severe_cough = input("\nDo you have severe cough?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_cough.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
        self.fainting = input("\nDo you faint occasionally?\nPlease type Yes/No\n")
        self.fainting = self.fainting.lower()
        self.declare(Fact(fainting = self.fainting.strip().lower()))


   
#, low body temperature,
# restlessness, 

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        self.fatigue = input("\nDo you experience fatigue occasionally?\nPlease type Yes/No\n")
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        self.headache = input("\nDo you experience headaches?\nPlease type Yes/No\n")
        self.headache = self.headache.lower()
        self.declare(Fact(headache = self.headache.strip().lower()))
    
    # @Rule(Fact(findDisease='true'), (Fact(headache = 'yes')),salience = 960)
    # def hasSevereheadache(self):yb
    #     self.severe_headache = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_headache = self.severe_headache.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        self.back_pain = input("\nDo you experience back pains?\nPlease type Yes/No\n")
        self.back_pain = self.back_pain.lower()
        self.declare(Fact(back_pain = self.back_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(sunken_eyes = W())),salience = 950)
    def hasSunkenEyes(self):
        self.sunken_eyes = input("\nDo you experience sunken eyes?\nPlease type Yes/No\n")
        self.sunken_eyes = self.sunken_eyes.lower()
        self.declare(Fact(sunken_eyes = self.sunken_eyes.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fever = W())),salience = 945)
    def hasfever(self):
        self.fever = input("\nDo you experience fever?\nPlease type Yes/No\n")
        self.fever=self.fever.lower()
        self.declare(Fact(fever = self.fever.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sore_throat = W())),salience = 940)
    def hassorethroat(self):
        self.sore_throat = input("\nDo you experience sore throat?\nPlease type Yes/No\n")
        self.sore_throat = self.sore_throat.lower()
        self.declare(Fact(sore_throat = self.sore_throat.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(restlessness = W())),salience = 935)
    def hasrestlessness(self):
        self.restlessness = input("\nDo you experience restlessness?\nPlease type Yes/No\n")
        self.restlessness = self.restlessness.lower()
        self.declare(Fact(restlessness = self.restlessness.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(bleeding_easily = W())),salience = 930)
    def hasbleeding_easily(self):
        self.bleeding_easily = input("\nDo you experience bleeding easily?\nPlease type Yes/No\n")
        self.bleeding_easily = self.bleeding_easily.lower()
        self.declare(Fact(bleeding_easily = self.bleeding_easily.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(bruising_easily = W())),salience = 925)
    def hasbruising_easily(self):
        self.bruising_easily = input("\nDo you experience bruising easily?\nPlease type Yes/No\n")
        self.bruising_easily = self.bleeding_easily.lower()
        self.declare(Fact(bruising_easily = self.bruising_easily.strip().lower()))
        
    @Rule(Fact(findDisease='true'), NOT (Fact(poor_appetite = W())),salience = 920)
    def haspoor_appetite(self):
        self.poor_appetite = input("\nDo you experience poor appetite?\nPlease type Yes/No\n")
        self.poor_appetite = self.poor_appetite.lower()
        self.declare(Fact(poor_appetite = self.poor_appetite.strip().lower()))  

    @Rule(Fact(findDisease='true'), NOT (Fact(dark_urine = W())),salience = 915)
    def hasdark_urine(self):
        self.dark_urine = input("\nDo you experience dark urine?\nPlease type Yes/No\n")
        self.dark_urine = self.dark_urine.lower()
        self.declare(Fact(dark_urine = self.dark_urine.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(swelling_in_the_legs = W())),salience = 910)
    def hasswelling_in_the_legs(self):
        self.swelling_in_the_legs = input("\nDo you experience swelling_in_the_legs?\nPlease type Yes/No\n")
        self.swelling_in_the_legs = self.swelling_in_the_legs.lower()
        self.declare(Fact(dark_urine = self.swelling_in_the_legs.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Weightless = W())),salience = 905)
    def hasWeightless(self):
        self.Weightless = input("\nDo you experience Weightless?\nPlease type Yes/No\n")
        self.Weightless = self.Weightless.lower()
        self.declare(Fact(Weightless = self.Weightless.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(difficulty_swallowing = W())),salience = 900)
    def hasdifficulty_swallowing(self):
        self.difficulty_swallowing = input("\nDo you experience difficulty_swallowing?\nPlease type Yes/No\n")
        self.difficulty_swallowing = self.difficulty_swallowing.lower()
        self.declare(Fact(difficulty_swallowings = self.difficulty_swallowing.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(increased_saliva = W())),salience = 895)
    def hasincreased_saliva(self):
        self.increased_saliva = input("\nDo you experience increased_saliva?\nPlease type Yes/No\n")
        self.increased_saliva = self.increased_saliva.lower()
        self.declare(Fact(increased_saliva = self.increased_saliva.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(ausea_and_vomiting = W())),salience = 890)
    def hasausea_and_vomiting(self):
        self.ausea_and_vomiting = input("\nDo you experience ausea_and_vomiting?\nPlease type Yes/No\n")
        self.ausea_and_vomiting = self.ausea_and_vomiting.lower()
        self.declare(Fact(ausea_and_vomiting = self.ausea_and_vomiting.strip().lower())) 

    @Rule(Fact(findDisease='true'), NOT (Fact(Breathing_problems = W())),salience = 885)
    def hasBreathing_problems(self):
        self.Breathing_problems = input("\nDo you experience Breathing_problems?\nPlease type Yes/No\n")
        self.Breathing_problems = self.Breathing_problems.lower()
        self.declare(Fact(tinnitus = self.Breathing_problems.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(tinnitus = W())),salience = 880)
    def hastinnitus(self):
        self.tinnitus = input("\nDo you experience tinnitus?\nPlease type Yes/No\n")
        self.tinnitus = self.tinnitus.lower()
        self.declare(Fact(tinnitus = self.tinnitus.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(laziness = W())),salience = 875)
    def haslaziness(self):
        self.laziness = input("\nDo you experience laziness?\nPlease type Yes/No\n")
        self.laziness = self.laziness.lower()
        self.declare(Fact(laziness = self.laziness.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fast_heartbeat = W())),salience = 870)
    def hasfast_heartbeats(self):
        self.fast_heartbeat = input("\nDo you experience fast heartbeat?\nPlease type Yes/No\n")
        self.fast_heartbeat = self.fast_heartbeat.lower()
        self.declare(Fact(fast_heartbeat = self.fast_heartbeat.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(over_weightt = W())),salience = 865)
    def hasoverweight(self):
        self.fast_over_weight = input("\nDo you experience overweight?\nPlease type Yes/No\n")
        self.fast_over_weight = self.fast_over_weight.lower()
        self.declare(Fact(over_weight = self.fast_over_weight.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(stomach_pain = W())),salience = 860)
    def hasstomach_pain(self):
        self.stomach_pain = input("\nDo you experience stomach pain?\nPlease type Yes/No\n")
        self.stomach_pain = self.stomach_pain.lower()
        self.declare(Fact(stomach_pain = self.stomach_pain.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(frequent_urination = W())),salience = 855)
    def hasfrequent_urination(self):
        self.frequent_urination = input("\nDo you experience frequent_urination?\nPlease type Yes/No\n")
        self.frequent_urination = self.frequent_urination.lower()
        self.declare(Fact(frequent_urination = self.frequent_urination.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(burning_urine = W())),salience = 850)
    def hasburning_urine(self):
        self.burning_urine = input("\nDo you experience burning urine?\nPlease type Yes/No\n")
        self.burning_urine = self.burning_urine.lower()
        self.declare(Fact(burning_urine = self.burning_urine.strip().lower())) 

    @Rule(Fact(findDisease='true'), NOT (Fact(blood_in_urine = W())),salience = 845)
    def hasblood_in_urine(self):
        self.blood_in_urine = input("\nDo you experience blood in urine?\nPlease type Yes/No\n")
        self.blood_in_urine = self.blood_in_urine.lower()
        self.declare(Fact(blood_in_urine = self.blood_in_urine.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Eye_burning = W())),salience = 840)
    def hasEye_burning(self):
        self.Eye_burning = input("\nDo you experience Eye_burning?\nPlease type Yes/No\n")
        self.Eye_burning = self.Eye_burning.lower()
        self.declare(Fact(Eye_burning = self.Eye_burning.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sensitivity_to_light = W())),salience = 835)
    def hassensitivity_to_light(self):
        self.sensitivity_to_light= input("\nDo you experience sensitivity_to_light?\nPlease type Yes/No\n")
        self.sensitivity_to_light = self.sensitivity_to_light.lower()
        self.declare(Fact(sensitivity_to_light = self.sensitivity_to_light.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(eye_redness = W())),salience = 830)
    def haseye_redness(self):
        self.eye_redness= input("\nDo you experience eye redness?\nPlease type Yes/No\n")
        self.eye_rednesst = self.eye_redness.lower()
        self.declare(Fact(eye_redness = self.eye_redness.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Feeling_of_having_something_in_the_eye = W())),salience = 825)
    def hasFeeling_of_having_something_in_the_eye(self):
        self.Feeling_of_having_something_in_the_eye= input("\nDo you experience Feeling_of_having_something_in_the_eye?\nPlease type Yes/No\n")
        self.Feeling_of_having_something_in_the_eye = self.Feeling_of_having_something_in_the_eye.lower()
        self.declare(Fact(Feeling_of_having_something_in_the_eye = self.Feeling_of_having_something_in_the_eye.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(Difficult_wearing_lenses = W())),salience = 820)
    def hasDifficulty_wearing_lenses(self):
        self.Difficulty_wearing_lenses= input("\nDo you experience Difficulty_wearing_lenses?\nPlease type Yes/No\n")
        self.Difficulty_wearing_lenses = self.Difficulty_wearing_lenses.lower()
        self.declare(Fact(Difficulty_wearing_lenses = self.Difficulty_wearing_lenses.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(blurred_vision = W())),salience = 815)
    def hasblurred_vision(self):
        self.blurred_vision= input("\nDo you experienceblurred_vision?\nPlease type Yes/No\n")
        self.blurred_vision = self.blurred_vision.lower()
        self.declare(Fact(blurred_vision = self.blurred_vision.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(incress_tears = W())),salience = 810)
    def hasincress_tears(self):
        self.incress_tears= input("\nDo you experience incress tears?\nPlease type Yes/No\n")
        self.incress_tears = self.incress_tears.lower()
        self.declare(Fact(incress_tears = self.incress_tears.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sebaceous_eye_bag = W())),salience = 805)
    def hassebaceous_eye_bag(self):
        self.sebaceous_eye_bag= input("\nDo you experience sebaceous_eye_bag?\nPlease type Yes/No\n")
        self.sebaceous_eye_bag = self.sebaceous_eye_bag.lower()
        self.declare(Fact(sebaceous_eye_bag = self.sebaceous_eye_bag.strip().lower())) 

    @Rule(Fact(findDisease='true'), NOT (Fact(Itchy_in_the_eye = W())),salience = 800)
    def hasItchy_in_the_eye(self):
        self.Itchy_in_the_eye= input("\nDo you experience Itchy in the eye?\nPlease type Yes/No\n")
        self.Itchy_in_the_eye = self.Itchy_in_the_eye.lower()
        self.declare(Fact(Itchy_in_the_eye = self.Itchy_in_the_eye.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Peeling_of_the_eyelid_skin = W())),salience = 795)
    def hasPeeling_of_the_eyelid_skin(self):
        self.Peeling_of_the_eyelid_skin= input("\nDo you experience Peeling_of_the_eyelid_skin?\nPlease type Yes/No\n")
        self.Peeling_of_the_eyelid_skin = self.Peeling_of_the_eyelid_skin.lower()
        self.declare(Fact(Peeling_of_the_eyelid_skin= self.Peeling_of_the_eyelid_skin.strip().lower())) 

    @Rule(Fact(findDisease='true'), NOT (Fact(eyelid_adhesion = W())),salience = 790)
    def haseyelid_adhesion(self):
        self.eyelid_adhesion= input("\nDo you experience eyelid_adhesion?\nPlease type Yes/No\n")
        self.eyelid_adhesion = self.eyelid_adhesion.lower()
        self.declare(Fact(eyelid_adhesion= self.eyelid_adhesion.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Increased_thirst_and_the_urge_to_urinate = W())),salience = 785)
    def hasIncreased_thirst_and_the_urge_to_urinate(self):
        self.Increased_thirst_and_the_urge_to_urinate= input("\nDo you experience Increased_thirst_and_the_urge_to_urinate?\nPlease type Yes/No\n")
        self.Increased_thirst_and_the_urge_to_urinate = self.Increased_thirst_and_the_urge_to_urinate.lower()
        self.declare(Fact(Increased_thirst_and_the_urge_to_urinate= self.Increased_thirst_and_the_urge_to_urinate.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Feelin_more_hungry = W())),salience = 785)
    def hasFeeling_more_hungry(self):
        self.Feeling_more_hungry= input("\nDo you experience Feeling_more_hungry?\nPlease type Yes/No\n")
        self.Feeling_more_hungry = self.Feeling_more_hungry.lower()
        self.declare(Fact(Feeling_more_hungry= self.Feeling_more_hungry.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Difficulty_healing_wounds = W())),salience = 780)
    def hasDifficulty_healing_wounds(self):
        self.Difficulty_healing_wounds= input("\nDo you experience Difficulty_healing_wounds?\nPlease type Yes/No\n")
        self.Difficulty_healing_wounds = self.Difficulty_healing_wounds.lower()
        self.declare(Fact(Difficulty_healing_wounds= self.Difficulty_healing_wounds.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Red_and_swollen_gums = W())),salience = 775)
    def hasRed_and_swollen_gums(self):
        self.Red_and_swollen_gums= input("\nDo you experience Red_and_swollen_gums?\nPlease type Yes/No\n")
        self.Red_and_swollen_gums = self.Red_and_swollen_gums.lower()
        self.declare(Fact(Red_and_swollen_gums= self.Red_and_swollen_gums.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Red_patches_of_skin_covered_with_silvery_scales= W())),salience = 770)
    def hasRed_patches_of_skin_covered_with_silvery_scales(self):
        self.Red_patches_of_skin_covered_with_silvery_scales= input("\nDo you experience Red_patches_of_skin_covered_with_silvery_scales?\nPlease type Yes/No\n")
        self.Red_patches_of_skin_covered_with_silvery_scales = self.Red_patches_of_skin_covered_with_silvery_scales.lower()
        self.declare(Fact(Red_patches_of_skin_covered_with_silvery_scales= self.Red_patches_of_skin_covered_with_silvery_scales.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Dry_skin= W())),salience = 765)
    def hasDry_skin(self):
        self.Dry_skin= input("\nDo you experience Dry skin?\nPlease type Yes/No\n")
        self.Dry_skin = self.Dry_skin.lower()
        self.declare(Fact(Dry_skin= self.Dry_skin.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(Nails_that_are_thick_or_have_pits_or_edges= W())),salience = 760)
    def hasNails_that_are_thick_or_have_pits_or_edges(self):
        self.Nails_that_are_thick_or_have_pits_or_edges= input("\nDo you experience Nails_that_are_thick_or_have_pits_or_edges?\nPlease type Yes/No\n")
        self.Nails_that_are_thick_or_have_pits_or_edges = self.Dry_skin.lower()
        self.declare(Fact(Nails_that_are_thick_or_have_pits_or_edges= self.Nails_that_are_thick_or_have_pits_or_edges.strip().lower()))  

    @Rule(Fact(findDisease='true'), NOT (Fact(Joint_swelling_or_stiffness= W())),salience = 755)
    def hasJoint_swelling_or_stiffness(self):
        self.Joint_swelling_or_stiffness= input("\nDo you experience Joint_swelling_or_stiffness?\nPlease type Yes/No\n")
        self.Joint_swelling_or_stiffness = self.Joint_swelling_or_stiffness.lower()
        self.declare(Fact(Joint_swelling_or_stiffness= self.Joint_swelling_or_stiffness.strip().lower()))                              


                                                                                                            
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headche = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_1(self):
        self.declare(Fact(disease = 'Alzheimers'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_2(self):
        self.declare(Fact(disease = 'Asthma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_3(self):
        self.declare(Fact(disease = 'Diabetes'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_4(self):
        self.declare(Fact(disease = 'Epilepsy'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_5(self):
        self.declare(Fact(disease = 'Glaucoma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_6(self):
        self.declare(Fact(disease = 'Heart Disease'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_7(self):
        self.declare(Fact(disease = 'Heat Stroke'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_8(self):
        self.declare(Fact(disease = 'Hyperthyroidism'))
    
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_9(self):
        self.declare(Fact(disease = 'Hypothermia'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_10(self):
        self.declare(Fact(disease = 'Jaundice'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_11(self):
        self.declare(Fact(disease = 'Sinusitis'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_12(self):
        self.declare(Fact(disease = 'Tuberculosis'))
    
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='yes'),Fact(bruising_easily ='yes'),Fact(poor_appetite='yes'),Fact(dark_urine='yes'),Fact(swelling_in_the_legs='yes'),Fact(Weightless='yes'))
    def disease_13(self):
        self.declare(Fact(disease = 'virus c')) 

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='yes'),Fact(increased_saliva='yes'))
    def disease_14(self):
        self.declare(Fact(disease = 'GERD'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='yes'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='yes'),Fact(difficulty_swallowing='yes'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='yes'),
    Fact(Breathing_problems='yes'))
    def disease_15(self):
        self.declare(Fact(disease = 'Germ_stomach'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'yes'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'),Fact (bleeding_easily='yes'),Fact(bruising_easily ='yes'),Fact(poor_appetite='yes'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='yes'),Fact(difficulty_swallowing='yes'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='yes'),
    Fact(Breathing_problems='yes'),Fact(tinnitus='yes'),Fact(laziness='yes'),Fact(fast_heartbeat='yes'))
    def disease_16(self):
        self.declare(Fact(disease = 'Hypertension'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='yes'),
    Fact(Breathing_problems='yes'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'))
    def disease_17(self):
        self.declare(Fact(disease = 'heart_attack'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='yes'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='yes'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'))
    def disease_18(self):
        self.declare(Fact(disease = 'Arteriosclerosis'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='yes'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='yes'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='yes'),Fact(overweight='yes'))
    def disease_19(self):
        self.declare(Fact(disease = 'heart failure'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'yes'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='no'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'),Fact(overweight='no'),Fact(stomach_pain='yes'),
    Fact(frequent_urination='yes'),Fact(burning_urine='yes'))
    def disease_20(self):
        self.declare(Fact(disease = 'kidney Inflammation'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'yes'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='yes'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='yes'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='no'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'),Fact(overweight='no'),Fact(stomach_pain='no'),
    Fact(frequent_urination='no'),Fact(burning_urine='no'),Fact(blood_in_urine='yes'))
    def disease_21(self):
        self.declare(Fact(disease = 'kidney cancer'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='no'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'),Fact(overweight='no'),Fact(stomach_pain='no'),
    Fact(frequent_urination='no'),Fact(burning_urine='no'),Fact(blood_in_urine='no'),Fact(Eye_burning='yes'),
    Fact(sensitivity_to_light='yes'),Fact(eye_redness='yes'),Fact(Feeling_of_having_something_in_the_eye='yes'),Fact(Difficulty_wearing_lenses='yes'),Fact(blurred_vision='yes'))
    def disease_22(self):
        self.declare(Fact(disease = 'dry eyes'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='no'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'),Fact(overweight='no'),Fact(stomach_pain='no'),
    Fact(frequent_urination='no'),Fact(burning_urine='no'),Fact(blood_in_urine='no'),Fact(Eye_burning='no'),
    Fact(sensitivity_to_light='yes'),Fact(eye_redness='yes'),Fact(Feeling_of_having_something_in_the_eye='yes'),Fact(Difficulty_wearing_lenses='no'),Fact(blurred_vision='yes'),
    Fact(incress_tears='yes'),Fact(sebaceous_eye_bag='yes'),Fact(Itchy_in_the_eye='yes'),Fact(Peeling_of_the_eyelid_skin='yes'),Fact(eyelid_adhesion='yes'))
    def disease_23(self):
        self.declare(Fact(disease = 'Blepharitis of the eye'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'),Fact (bleeding_easily='no'),Fact(bruising_easily ='no'),Fact(poor_appetite='no'),Fact(dark_urine='no'),Fact(swelling_in_the_legs='no'),Fact(Weightless='no'),Fact(difficulty_swallowing='no'),Fact(increased_saliva='no'),Fact(ausea_and_vomiting='no'),
    Fact(Breathing_problems='no'),Fact(tinnitus='no'),Fact(laziness='no'),Fact(fast_heartbeat='no'),Fact(overweight='no'),Fact(stomach_pain='no'),
    Fact(frequent_urination='no'),Fact(burning_urine='no'),Fact(blood_in_urine='no'),Fact(Eye_burning='no'),
    Fact(sensitivity_to_light='no'),Fact(eye_redness='no'),Fact(Feeling_of_having_something_in_the_eye='no'),Fact(Difficulty_wearing_lenses='no'),Fact(blurred_vision='no'),
    Fact(incress_tears='no'),Fact(sebaceous_eye_bag='no'),Fact(Itchy_in_the_eye='no'),Fact(Peeling_of_the_eyelid_skin='no')
    ,Fact(eyelid_adhesion='no'),Fact(Red_patches_of_skin_covered_with_silvery_scales='yes'),Fact(Dry_skin='yes'),Fact(Nails_that_are_thick_or_have_pits_or_edges='yes')
    ,Fact(Joint_swelling_or_stiffness='yes'))
    def disease_24(self):
        self.declare(Fact(disease = 'psoriasis')) 


    @Rule(Fact(findDisease='true'),NOT (Fact(disease = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = 1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            mapDisease = []
            mapDisease.append('back_pain')
            mapDisease.append('chest_pain')
            mapDisease.append('cough')
            mapDisease.append('fainting')
            mapDisease.append('fatigue')
            mapDisease.append('fever')
            mapDisease.append('headache')
            mapDisease.append('sore_throat')
            mapDisease.append('restlessness')
            mapDisease.append('sunken_eyes')
            mapDisease.append('bleeding_easily')
            mapDisease.append('bruising_easily')
            mapDisease.append('poor_appetite')
            mapDisease.append('dark_urine')
            mapDisease.append('swelling_in_the_legs')
            mapDisease.append('Weightless')
            mapDisease.append('difficulty_swallowing')
            mapDisease.append('increased_saliva')
            mapDisease.append('ausea_and_vomiting')
            mapDisease.append('Breathing_problems')
            mapDisease.append('tinnitus')
            mapDisease.append('laziness')
            mapDisease.append('fast_heartbeat')
            mapDisease.append('overweight')
            mapDisease.append('stomach_pain')
            mapDisease.append('frequent_urination')
            mapDisease.append('burning_urine')
            mapDisease.append('blood_in_urine')
            mapDisease.append('Eye_burning')
            mapDisease.append('sensitivity_to_light')
            mapDisease.append('eye_redness')
            mapDisease.append('Feeling_of_having_something_in_the_eye')
            mapDisease.append('Difficulty_wearing_lenses')
            mapDisease.append('blurred_vision')
            mapDisease.append('incress_tears')
            mapDisease.append('sebaceous_eye_bag')
            mapDisease.append('Peeling_of_the_eyelid_skin')
            mapDisease.append('eyelid_adhesion')
            mapDisease.append('Increased_thirst_and_the_urge_to_urinate')
            mapDisease.append('Feeling_more_hungry')
            mapDisease.append('Difficulty_healing_wounds')
            mapDisease.append('Red_and_swollen_gums')
            mapDisease.append('Red_patches_of_skin_covered_with_silvery_scales')
            mapDisease.append('Dry_skin')
            mapDisease.append('For itching, burning, or soreness')
            mapDisease.append('Nails_that_are_thick_or_have_pits_or_edges')
            mapDisease.append('Joint_swelling_or_stiffness')


            print('\n\nWe checked the following symptoms',mapDisease)
            mapDisease_val=[self.back_pain,self.chest_pain,self.cough,self.fainting,self.fatigue
            ,self.fever,self.headache,self.sore_throat,self.restlessness,self.sunken_eyes,self.bruising_easily,self.bleeding_easily,
            self.poor_appetite,self.dark_urine,self.swelling_in_the_legs,self.Weightless,self.difficulty_swallowing,
            self.increased_saliva,self.ausea_and_vomiting,self.Breathing_problems,self.laziness,
            self.fast_heartbeat,self.fast_over_weight,self.stomach_pain,self.frequent_urination,self.burning_urine,
            self.blood_in_urine,self.Eye_burning,self.sensitivity_to_light,self.eye_redness,self.Feeling_of_having_something_in_the_eye,
            self.Difficulty_wearing_lenses,self.blurred_vision,self.incress_tears,self.sebaceous_eye_bag,self.Itchy_in_the_eye,
            self.Peeling_of_the_eyelid_skin,self.eyelid_adhesion,self.Increased_thirst_and_the_urge_to_urinate,
            self.Feeling_more_hungry,self.Difficulty_healing_wounds,self.Red_and_swollen_gums,self.Red_patches_of_skin_covered_with_silvery_scales,
            self.Dry_skin,self.Nails_that_are_thick_or_have_pits_or_edges,self.Joint_swelling_or_stiffness]
            print('\n\nSymptoms in patients are :', mapDisease_val)
            
            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()
            
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'yes':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            print('\n\nYes symptoms noticed are : ', yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_symptoms:
                        count+=1
                #print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                print("No diseases found.You are healthy!")
            else:
                print("\n\nWe are unable to tell you the exact disease with confidence.But we believe that you suffer from",pred_dis)
                
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')

                print ('\n\nSome info about the disease:',pred_dis)
                
                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r")
                print(f.read())
                print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r")
                print(f.read())
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
        else:
            print('The most probable illness you are suffering from is:',disease)
            print('\n\n')
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('Some info about the disease:\n')
            print(disease)
            f = open("disease/disease_descriptions/" + disease + ".txt", "r")
            print(f.read())
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
            f = open("disease/disease_treatments/" + disease + ".txt", "r")
            print(f.read())
    # @Rule(Fact(findDisease = 'true'),
    # Fact(name=MATCH.name))
    # def greet(self, name):
    #     print("Hi!",name, "How is the weather?")
if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print('Printing engine facts after 1 run',engine.facts)
   