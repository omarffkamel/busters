# Character Definitions
define narrator = Character(None)
define whistleblower = Character("Whistleblower")
define suspect1 = Character("Aaron")
define suspect2 = Character("Sophie")
define suspect3 = Character("Marcus")
define suspect4 = Character("Claire")
define suspect5 = Character("Dylan")
define suspect6 = Character("Rebecca")
define suspect7 = Character("Ethan")
define suspect8 = Character("Lila")
define suspect9 = Character("Julian")


# Set up initial variables
default suspect_choice = ""
default initial_suspect = ""

# The game starts here
label start:

    # Introduction Scene
    scene office_day with fade

    whistleblower "Alex, a terrible crime has occurred at the Blackwood estate."
    whistleblower "Evelyn Blackwood was found murdered in her own garden."
    whistleblower "Three individuals are under suspicion. It's up to you to uncover the truth."

    # Present Suspects
    show suspect1 at Position(xalign=0.25, yalign=0.5)
    show suspect2 at Position(xalign=0.5, yalign=0.5)
    show suspect3 at Position(xalign=0.75, yalign=0.5)

    whistleblower "These are the three suspects in the case:"

    suspect1 "Aaron Vance, the groundskeeper with a heavy criminal record."
    suspect2 "Sophie Blackwood, Evelyn's stepdaughter, poised to inherit her fortune."
    suspect3 "Marcus Hale, Evelyn's longtime business partner."

    hide suspect1
    hide suspect2
    hide suspect3

    # Ask for Initial Hunch
    whistleblower "Based on this information, who do you initially suspect?"

    menu:
        "Aaron Vance":
            $ initial_suspect = "Aaron"
            whistleblower "Let's see where the evidence leads."
            jump aaron_scenario
        "Sophie Blackwood":
            $ initial_suspect = "Sophie"
            whistleblower "Let's see where the evidence leads."
            jump sophie_scenario
        "Marcus Hale":
            $ initial_suspect = "Marcus"
            whistleblower "Let's see where the evidence leads."
            jump marcus_scenario

label aaron_scenario:

    scene garden_day with fade
    whistleblower "You decide to focus your initial investigation on Aaron. He is the estate's groundskeeper and has a troubled past."
    narrator "You find Aaron in the garden, busy tending to a flower bed. He seems irritated as you approach."

    menu:
        "Where were you when Evelyn was killed?":
            suspect1 "I was out here, working as usual. No one was around to see me, though."
            narrator "You notice dirt under Aaron's fingernails and a fresh cut on his hand."
            menu:
                "Ask about the cut":
                    suspect1 "It’s nothing. I slipped while using the shears. I get cuts all the time. It’s part of the job."
                    narrator "Aaron seems defensive, but his explanation sounds plausible."
                "Ignore the cut":
                    narrator "You decide not to press him about the cut for now."
        "Did you and Evelyn get along?":
            suspect1 "She wasn’t my biggest fan, let’s put it that way. She always looked at me like I was a liability. But I stayed out of her way."
            narrator "Aaron shifts uncomfortably, avoiding eye contact."
        "Did you notice anything strange that day?":
            suspect1 "I did see Marcus leaving the house in a hurry earlier. Said something about a meeting in the city. I don’t trust him, though."
            narrator "Aaron shrugs. His comment about Marcus seems worth noting."

    narrator "As you leave, you notice a torn piece of fabric caught on a bush near the garden. It matches the color of Aaron’s uniform."
    narrator "You make a mental note of these details and decide to move on to the next suspect."

    jump sophie_investigation

label sophie_investigation:

    scene mansion_livingroom with fade
    whistleblower "You decide to interview Sophie next. She’s in the living room, appearing distraught but composed."
    narrator "She looks up at you, her eyes red from crying."

    menu:
        "Where were you during the time of the murder?":
            suspect2 "I was in my room, reading a book. I didn’t hear anything unusual."
            narrator "You glance at the book on the table. It’s open but covered in dust, suggesting it hasn’t been touched recently."
        "You stand to inherit a lot, don’t you?":
            suspect2 "Is that what this is about? Money? Evelyn was family to me, no matter how difficult she could be. Money can’t replace that."
            narrator "Sophie wipes away a tear, but her trembling hands betray her emotions."
        "Did Evelyn have enemies?":
            suspect2 "She didn’t trust many people, but Marcus... he’s the one you should be looking at. They’ve been arguing for weeks over the company."
            narrator "Sophie’s answer aligns with Aaron’s earlier comment about Marcus."

    narrator "As you look around the room, you notice a family portrait on the wall. Evelyn’s face has been scratched out, raising your suspicions."
    narrator "Sophie excuses herself, saying she needs a moment alone. You decide to follow up with Marcus."

    jump marcus_investigation

label marcus_investigation:

    scene markus_room with fade
    whistleblower "You find Marcus in his office, calmly organizing some papers. He greets you with a confident smile."
    narrator "The room smells faintly of cigar smoke, and his desk is cluttered with documents."

    menu:
        "Where were you when Evelyn was killed?":
            suspect3 "I was in the city for a meeting. I didn’t get back until late in the evening."
            narrator "You glance at his open calendar and notice that no appointments are listed for that day."
        "Did you and Evelyn have disagreements?":
            suspect3 "Disagreements? No, not at all. We were successful business partners. Disputes come with the territory, but nothing serious."
            narrator "Marcus smiles slightly, but his tone feels rehearsed."
        "Why is Evelyn’s name on this paper?":
            suspect3 "That’s just business documentation. Evelyn and I were negotiating a buyout of her shares. It’s all perfectly legal."
            narrator "The unsigned contracts in his briefcase suggest otherwise. The terms appear aggressive, almost coercive."

    narrator "You make a mental note of his unease and decide to wrap up the interview."
    jump confront_marcus

label confront_marcus:

    scene markus_room with fade
    whistleblower "You confront Marcus with the evidence you’ve gathered."
    narrator "Marcus tries to maintain his composure, but the cracks in his story begin to show."

    "“Marcus, I found unsigned contracts in your briefcase. Evelyn wasn’t happy with your terms, was she?”"
    suspect3 "Look, those were just business negotiations. Nothing more."
    "“Negotiations, or coercion? Evelyn was planning to reject your offer, wasn’t she?”"
    suspect3 "This is absurd. You have no proof of anything. I’ve been a loyal partner to Evelyn for years."
    "“Loyal? Then why did she tell her lawyer she feared for her safety the day before she died?”"
    suspect3 "This is ridiculous.."

    jump marcus_arrested

label marcus_arrested:

    scene police_station_night with fade

    narrator "Marcus was arrested for the murder of Evelyn Blackwood."

    whistleblower "Well, even I suspected Aaron was the criminal but perhaps the obvious choice isn't always the correct one after all..."
    whistleblower "Why don't we move to your next case?"
    
    # Display a menu for the next case
    menu:
        "Proceed to the Next Case":
            jump library
        "End Game":
            return

    return
label sophie_scenario:

    scene mansion_livingroom with fade
    whistleblower "You decide to focus your initial investigation on Sophie. As Evelyn’s stepdaughter and the potential heir to her fortune, she seems like a plausible suspect."
    narrator "You find Sophie in the living room, sitting on a velvet chair. She looks upset but composed, her hands clasped tightly."

    menu:
        "Where were you during the murder?":
            suspect2 "I was in my room, reading a book. I didn’t hear anything unusual."
            narrator "You glance at the book on the table nearby. It looks like it hasn’t been touched recently, with a light layer of dust on its surface."
        "Did you and Evelyn get along?":
            suspect2 "We had our differences, sure, but she was family. Money doesn’t replace that."
            narrator "Sophie’s words seem genuine, but her body language suggests she’s holding back."
        "Did Evelyn have enemies?":
            suspect2 "She didn’t trust many people, especially Marcus. They’ve been arguing for weeks about the company."
            narrator "Her statement aligns with Aaron’s earlier comment about Marcus. However, it doesn’t fully absolve her."

    narrator "As you leave, you notice a framed family photo on the wall. Evelyn’s face has been scratched out, adding to the tension around Sophie’s potential motive."
    narrator "You decide to interview Marcus next to gather more information."

    jump marcus_investigation_2

label marcus_investigation_2:

    scene markus_room with fade
    whistleblower "You decide to question Marcus next. He’s in his office, organizing papers. He greets you with a professional smile, though his expression is tense."
    narrator "The room smells faintly of cigar smoke, and Marcus’s desk is cluttered with business documents."

    menu:
        "Where were you when Evelyn was killed?":
            suspect3 "I was in the city for a meeting. I didn’t get back until late in the evening."
            narrator "You glance at his open calendar and notice that no appointments are listed for that day."
        "Did you and Evelyn have disagreements?":
            suspect3 "We had our fair share of business disputes, but nothing personal. It was just business."
            narrator "Marcus’s tone is calm, but his rehearsed manner raises suspicions."
        "What’s with these unsigned contracts?":
            suspect3 "Those were part of a negotiation. Evelyn was considering selling her shares in the company. It’s all above board."
            narrator "The documents suggest aggressive terms, making it seem like Marcus might have been pressuring Evelyn."

    narrator "As you leave Marcus’s office, you notice a muddy footprint near the back door, leading to the garden. You decide to confront Aaron about this discovery."

    jump aaron_confrontation

label aaron_confrontation:

    scene garden_day with fade
    whistleblower "Your investigation takes you back to Aaron, whose earlier comments about Marcus now seem suspect."
    narrator "You find Aaron in the garden, pruning hedges. He looks up, clearly annoyed by your return."

    menu:
        "Where were you during the murder?":
            suspect1 "I already told you—I was here, working. Nobody saw me, but that doesn’t mean anything!"
            narrator "His defensiveness only increases your suspicion."
        "What’s with the cut on your hand?":
            suspect1 "It’s from pruning. I use sharp tools all the time—it’s normal to get cuts."
            narrator "His explanation is plausible, but his irritated tone suggests he’s hiding something."
        "How do you explain the muddy footprint by the back door?":
            suspect1 "What footprint? I don’t know anything about that."
            narrator "Aaron’s evasive answer doesn’t match the evidence, raising more questions."

    narrator "As you press Aaron further, he begins to crack under the pressure. Eventually, he blurts out a confession."

    suspect1 "Fine! I did it! Evelyn was going to fire me after all I’ve done for this place. I couldn’t let her ruin my life like that."
    narrator "Aaron’s confession leaves no doubt about his guilt. You quickly inform the authorities."

    jump case_resolved_aaron

label case_resolved_aaron:

    scene police_station_night with fade
    whistleblower "Aaron has been arrested for the murder of Evelyn Blackwood."
    whistleblower "It seems this time, the person with the obvious motive wasn’t the guilty party after all."
    whistleblower "Great work, Alex. Are you ready to move on to the next case?"

    menu:
        "Proceed to the Next Case":
            jump library
        "End Game":
            return

    return
label marcus_scenario:

    scene markus_room with fade
    whistleblower "You decide to focus on Marcus first. As Evelyn’s business partner, he had a clear motive related to their company’s disputes."
    narrator "You find Marcus in his office, organizing papers. He greets you with a confident smile, but there’s tension in his demeanor."

    menu:
        "Where were you during the murder?":
            suspect3 "I was in the city for a meeting. I didn’t get back until late in the evening."
            narrator "His alibi seems shaky, as his open calendar shows no appointments for the day."
        "Did you and Evelyn have disagreements?":
            suspect3 "We argued about business, sure, but that’s normal for partners. It was never personal."
            narrator "Marcus’s tone is even, but the aggressive terms in his unsigned contracts tell a different story."
        "What about Sophie? Could she have done this?":
            suspect3 "Sophie? She stands to inherit everything. If you ask me, you should take a closer look at her."
            narrator "His suggestion raises questions about Sophie’s motives."

    narrator "As you leave Marcus’s office, you notice a muddy footprint near the back door, leading to the garden. You decide to speak with Aaron next."

    jump aaron_investigation

label aaron_investigation:

    scene garden_day with fade
    whistleblower "Next, you turn your attention to Aaron. As the estate’s groundskeeper, he knows the property better than anyone else."
    narrator "You find Aaron in the garden, tending to a flower bed. He looks up, frowning as you approach."

    menu:
        "Where were you during the murder?":
            suspect1 "I was here, working. No one saw me, but that doesn’t mean I did anything wrong!"
            narrator "Aaron’s defensiveness doesn’t do him any favors."
        "What’s with the cut on your hand?":
            suspect1 "It’s from pruning. I get cuts all the time—it’s part of the job."
            narrator "His explanation is plausible, but his tone suggests he’s on edge."
        "Did you notice anything suspicious that day?":
            suspect1 "Sophie was acting weird. She kept pacing around the garden, talking to herself. I didn’t want to get involved."
            narrator "Aaron’s comment about Sophie raises your suspicion."

    narrator "As you leave the garden, you notice a torn piece of fabric caught on a bush. It matches Sophie’s clothing."
    narrator "You decide it’s time to confront Sophie directly."

    jump sophie_confrontation

label sophie_confrontation:

    scene mansion_livingroom with fade
    whistleblower "With mounting evidence against Sophie, you decide to confront her. She’s sitting in the living room, visibly tense."
    narrator "Sophie looks up at you, her eyes narrowing."

    menu:
        "Where were you during the murder?":
            suspect2 "I told you, I was in my room, reading. Why do you keep asking me this?"
            narrator "Her tone is defensive, and the dust on the book nearby contradicts her claim."
        "How do you explain the torn fabric in the garden?":
            suspect2 "What? I—I must have snagged my dress earlier. That doesn’t mean anything!"
            narrator "Her explanation is weak, and she starts to fidget under your gaze."
        "Why was Evelyn’s face scratched out in the family photo?":
            suspect2 "Because she was cruel! She treated me like I was nothing, even after everything I’ve done for this family."
            narrator "Sophie’s anger slips through, revealing a deeper resentment toward Evelyn."

    narrator "As you press Sophie further, her composure crumbles. Eventually, she breaks down and confesses."

    suspect2 "Alright, I admit it! Evelyn always held the inheritance over my head. She deserved what she got!"
    narrator "Sophie’s confession leaves no doubt about her guilt. You quickly inform the authorities."

    jump case_resolved_sophie

label case_resolved_sophie:

    scene police_station_night with fade
    whistleblower "Sophie has been arrested for the murder of Evelyn Blackwood."
    whistleblower "It seems this time, the criminal was the one hiding in plain sight all along."
    whistleblower "Excellent work, Alex. Are you ready to move on to the next case?"

    menu:
        "Proceed to the Next Case":
            jump library
        "End Game":
            return

    return


label library:

    # Introduction to the second case
    scene library_exterior_day with fade

    whistleblower "We have a new case on our hands. A priceless manuscript has been stolen from the Blackwood Library."
    whistleblower "The theft occurred during a private event last night, and three individuals are under suspicion."

    # Present new suspects
    show suspect4 at Position(xalign=0.25, yalign=0.5)
    show suspect5 at Position(xalign=0.5, yalign=0.5)
    show suspect6 at Position(xalign=0.75, yalign=0.5)

    whistleblower "These are the three suspects in the case:"

    suspect4 "Claire Bennett, the librarian and the only one of the suspects with access to the manuscript"
    suspect5 "Dylan Bennett, Claire's husband, a rare books dealer, recently lost a lawsuit against the library for ownership of the manuscript."
    suspect6 "Rebecca Moore, a historian who recently published a book referencing the manuscript."

    hide suspect4
    hide suspect5
    hide suspect6

    # Ask for Initial Hunch
    whistleblower "Based on this information, who do you initially suspect?"

    menu:
        "Claire Bennett":
            $ initial_suspect = "Claire"
            whistleblower "Let's see where the evidence leads."
            jump claire_scenario
        "Dylan Cole":
            $ initial_suspect = "Dylan"
            whistleblower "Let's see where the evidence leads."
            jump dylan_scenario
        "Rebecca Moore":
            $ initial_suspect = "Rebecca"
            whistleblower "Let's see where the evidence leads."
            jump rebecca_scenario

label claire_scenario:

    scene library_archive_room with fade
    whistleblower "You decide to focus your initial investigation on Claire. As the library archivist, she had full access to Manuscript."
    narrator "Claire is in the archive room, carefully sorting through books. She looks nervous as you approach."

    menu:
    
        "Where were you during the theft?":
            suspect4 "I was in the archive room all night, cataloging. I didn’t leave until I heard the commotion."
            narrator "Her alibi seems weak, as no one else was around to verify her claim."
        "Did you have any reason to steal the Manuscript?":
            suspect4 "Of course not! My job is to protect these artifacts. Why would I jeopardize that?"
            narrator "Her answer is defensive, but her voice wavers slightly."
        "Did you notice anything unusual that night?":
            suspect4 "I heard someone near the back exit, but by the time I checked, no one was there. Maybe Dylan had something to do with it."
            narrator "Claire’s comment about Dylan seems worth investigating."

    narrator "As you leave, you notice a small leather bookmark on the floor. It looks old and out of place."
    narrator "You make a mental note of these details and decide to move on to the next suspect."

    jump dylan_investigation

label dylan_investigation:

    scene library_lounge with fade
    whistleblower "You decide to interview Dylan next. He’s in the library lounge, sipping coffee and looking irritated."
    narrator "Dylan looks up as you approach, his face hardening."

    menu:
        "Where were you during the theft?":
            suspect5 "I was in the reading room. Ask anyone there. I wasn’t even near the archive."
            narrator "His alibi might check out, but his tone suggests he’s hiding something."
        "Do you have any interest in the Manuscript?":
            suspect5 "Who wouldn’t? But I’m a collector, not a thief. I deal in legitimate acquisitions only."
            narrator "His reputation says otherwise, but his confidence is hard to shake."
        "Did you notice anything suspicious that night?":
            suspect5 "Rebecca was acting odd. She kept going back and forth between rooms, muttering to herself."
            narrator "Dylan’s statement about Rebecca raises more questions."

    narrator "As you glance at his bag, you notice a faint ink stain on the handle, matching the ink used in the Codex annotations."
    narrator "You decide to investigate Rebecca next."

    jump rebecca_investigation

label rebecca_investigation:

    scene library_reading_room with fade
    whistleblower "Rebecca is sitting in the reading room, poring over a stack of notes. She looks up with a forced smile as you approach."

    menu:
        "Where were you during the theft?":
            suspect6 "I was right here, studying. I had no reason to go near the archive."
            narrator "Rebecca’s alibi seems plausible, but her fidgeting hands suggest she’s nervous."
        "You’ve written about Manuscript, haven’t you?":
            suspect6 "Yes, but that doesn’t mean I’d steal it! My work is about preserving knowledge, not taking it."
            narrator "Her voice rises defensively, drawing glances from nearby patrons."
        "Did you see anything unusual that night?":
            suspect6 "I saw Claire near the back exit. She looked like she was in a hurry, but I didn’t think much of it at the time."
            narrator "Rebecca’s statement aligns with Claire’s earlier comment about the back exit."

    narrator "As you leave, you notice a torn page sticking out of Rebecca’s notebook. It looks suspiciously similar to the Manuscript’s pages."
    narrator "You now have enough evidence to start piecing things together."

    jump suspect_confrontation

label suspect_confrontation:

    scene library_meeting_room with fade
    whistleblower "It’s time to confront the suspects and determine who is responsible for the theft of the Manuscript."

    menu:
        "Confront Claire":
            narrator "You present the evidence of the bookmark found in the archive room."
            suspect4 "Alright, I admit it! I took the Manuscript, but only to protect it. Dylan was planning to sell it!"
            narrator "Claire’s confession implicates Dylan as well."
            jump case_resolved
        "Confront Dylan":
            narrator "You present the ink-stained bag as evidence."
            suspect5 "This is ridiculous! Claire planted that ink to frame me. I didn’t steal anything!"
            narrator "Dylan’s denial raises questions, but the evidence against him is compelling."
            jump case_resolved
        "Confront Rebecca":
            narrator "You present the torn page from Rebecca’s notebook."
            suspect6 "You’ve got it all wrong! I was just studying the Manuscript for my research. I didn’t steal it!"
            narrator "Rebecca’s defense is weak, but her motives seem more academic than malicious."
            jump case_resolved

label case_resolved:

    scene library_exterior_day with fade
    whistleblower "With the thief identified and the Codex recovered, justice has been served once again."
    whistleblower "Great work. Are you ready for the next challenge?"


    return


label dylan_scenario:

    scene library_lounge with fade
    narrator "You find Dylan in the library lounge, sipping coffee and scrolling through his phone. He looks up as you approach, raising an eyebrow."

    menu:
        "Where were you during the theft?":
            "I was in the reading room all night. There were plenty of people around to confirm that."
            narrator "His alibi seems solid, but his irritated tone suggests he’s not happy about being questioned."
        "You lost a lawsuit over the Manuscript, didn't you?":
            "The lawsuit was a joke. That manuscript was never rightfully theirs, but that doesn’t mean I’d steal it."
            narrator "Dylan’s bitterness is clear, but his words lack any direct admission of guilt."
        "Did you notice anything unusual that night?":
            "Rebecca. She kept pacing around and mumbling about deadlines. It was odd enough that I almost said something."
            narrator "Dylan’s comment puts Rebecca under scrutiny, but it doesn’t absolve him."

    menu:
        "Investigate Rebecca next.":
            jump rebecca_interview
        "Double back to check Claire’s alibi.":
            jump claire_interview

label rebecca_interview:

    scene library_reading_room with fade
    narrator "You decide to follow up on Dylan’s comment about Rebecca. She’s in the reading room, surrounded by books and scribbling furiously in her notebook."

    menu:
        "Where were you during the theft?":
            "Right here, doing research. I didn’t leave this room all night."
            narrator "Her alibi seems plausible, but her hurried tone raises suspicion."
        "You’ve referenced the Manuscript in your work, with a little too much interest, didn't you?":
            "I’m a historian, not a thief. My work respects artifacts—it doesn’t destroy them."
            narrator "Rebecca’s defensive tone feels rehearsed, but it doesn’t confirm guilt."
        "Did you see Dylan or Claire behaving suspiciously?":
            "I saw Dylan near the archive earlier. He looked like he was sneaking around. I didn’t think much of it then, but maybe you should ask him."
            narrator "Rebecca’s attempt to redirect suspicion onto Dylan feels calculated."

    narrator "As you glance at Rebecca’s table, you notice a scrap of paper tucked under her notebook. It has strange markings that resemble annotations from the Codex."

    menu:
        "Investigate Claire next.":
            jump claire_interview
        "Confront Dylan with Rebecca’s testimony.":
            jump dylan_confrontation

label claire_interview:

    scene library_archive_room with fade
    narrator "Claire, the librarian, is the next person you decide to question. Her position gave her direct access to the Codex, making her a key suspect."

    menu:
        "Where were you during the theft?":
            "I was here, cataloging books all night. I didn’t hear or see anything until the commotion."
            narrator "Claire’s alibi remains unverified, and her nervous demeanor isn’t helping her case."
        "Did you see Dylan or Rebecca near the archives?":
            "I saw Rebecca. She looked like she was in a hurry, heading toward the back exit. I didn’t see Dylan at all."
            narrator "Claire’s statement aligns with Dylan’s earlier comment about Rebecca."
        "Would you have any reason to steal the Codex?":
            "I protect artifacts, not steal them. Losing it would ruin my career!"
            narrator "Her voice shakes slightly, though her words suggest genuine concern."

    narrator "You notice a small bookmark on the floor near Claire’s desk. It’s made of leather and has faint markings that match the Codex."

    menu:
        "Confront Dylan with Rebecca’s and Claire’s accusations.":
            jump dylan_confrontation
        "Investigate Rebecca further, using Claire’s testimony.":
            jump rebecca_final_investigation

label dylan_confrontation:

    scene library_lounge with fade
    narrator "Armed with statements from Rebecca and Claire, you confront Dylan again. He looks visibly annoyed as you approach."

    menu:
        "Present the ink-stained bag as evidence.":
            narrator "You show Dylan the ink stain on his bag, suggesting it matches the Codex annotations."
            "That’s absurd! Rebecca was the one acting suspiciously, not me."
            narrator "Dylan’s denial feels panicked, but it shifts the focus back to Rebecca."
        "Ask about Rebecca’s pacing near the archives.":
            "She was definitely up to something. I even saw her stuffing something into her bag when she thought no one was looking."
            narrator "Dylan’s comment about Rebecca aligns with other evidence, making her the prime suspect."

    narrator "You decide to confront Rebecca directly, armed with the evidence gathered so far."

    jump rebecca_final_investigation

label rebecca_final_investigation:

    scene library_reading_room with fade
    narrator "You return to Rebecca, determined to get to the truth. She looks up, her face pale as you approach."

    menu:
        "Present the torn page from her notebook.":
            narrator "You produce the torn page, pointing out its resemblance to the Codex."
            "I—I found it on the floor near the archive! I was going to return it, I swear!"
            narrator "Her excuse is flimsy, and her panicked tone betrays her guilt."
        "Confront her about pacing near the archives.":
            "I wasn’t pacing! I was just... distracted. This research is important to me!"
            narrator "Rebecca’s evasive answer only deepens your suspicion."


    scene black with fade
    narrator "Upon further invesigation, Rebecca is arrested on the grounds of theft and tampering with historical artifacts."
    whistleblower "It is interesting that the obvious choice turned out to be false again, isn't it?"
    whistleblower "Would you like to move on with the final case"

    menu:
        "Move on to the Final Case.":
            jump final_case

        "End Game":
            return 

    return

label rebecca_scenario:

    scene library_reading_room with fade
    whistleblower "You decide to focus your initial investigation on Rebecca. As a historian who recently published a book referencing the Codex, she had a vested interest in the manuscript."
    narrator "You find Rebecca in the reading room, surrounded by a stack of notes. She looks up and greets you with a nervous smile."

    menu:
        "Where were you during the theft?":
            suspect6 "I was here all evening, researching for my next project. I didn’t leave this room."
            narrator "Her alibi sounds plausible, but you notice her hands trembling slightly as she speaks."
        "Why would you want the Manuscript?":
            suspect6 "Want it? Of course, I want access to it for my work, but stealing it? That’s absurd! My credibility would be ruined if I were caught."
            narrator "Rebecca’s defensive tone suggests she’s trying to hide something."
        "Did you notice anything suspicious?":
            suspect6 "I saw Dylan near the archive earlier. He looked like he was up to something, but I didn’t want to get involved."
            narrator "Rebecca shifts the blame to Dylan, but her nervousness makes you question her motives."

    narrator "As Rebecca speaks, you notice a small tear in one of her notebook pages. The edge matches the torn page found in the archive room."
    narrator "You make a mental note of her behavior and the evidence as you decide how to proceed."

    menu:
        "Press Rebecca further about the torn page.":
            suspect6 "Fine, yes! I took a closer look at the manuscript, but I didn’t take it! I swear!"
            narrator "Her partial admission doesn’t absolve her but adds complexity to her involvement."
        "Investigate Claire next.":
            jump claire_investigation
        "Investigate Dylan next.":
            jump dylan_investigation

    return


label final_case:

    scene council_hall_day with fade

    whistleblower "Alex, we've got a delicate situation on our hands."
    whistleblower "A confidential draft proposal outlining budget cuts for community programs has been leaked online."
    whistleblower "This leak has caused a public uproar, and the council is scrambling to control the damage."
    whistleblower "Your task is to find out how this happened, who is responsible, and why."

    narrator "The draft, which was still under review, contained speculative ideas such as job cuts, funding reallocations, and controversial project cancellations."
    narrator "Now, the public is demanding answers, and the council is desperate to regain trust."

    whistleblower "Here are the three individuals who had access to the draft and could be involved in the leak."

    # Present Suspects
    show suspect7 at Position(xalign=0.25, yalign=0.5)
    show suspect8 at Position(xalign=0.5, yalign=0.5)
    show suspect9 at Position(xalign=0.75, yalign=0.5)

    whistleblower "These are the suspects in this case:"

    suspect7 "Ethan Banks, a council member who has been critical of the current leadership."
    suspect8 "Lila Montgomery, a junior intern who was tasked with managing the draft and distributing printed copies to council members."
    suspect9 "Julian Sterling, an administrative officer responsible for organizing council documents."


    hide suspect7
    hide suspect8
    hide suspect9

    whistleblower "Based on this information, who do you initially suspect?"

    menu:
        "Ethan Banks":
            $ initial_suspect = "Ethan"
            whistleblower "Let's start with Ethan and see where the trail leads."
            jump ethan_sceario
        "Lila Montgomery":
            $ initial_suspect = "Lila"
            whistleblower "Let's start with Lila and see where the trail leads."
            jump lila_scenario
        "Julian Sterling":
            $ initial_suspect = "Julian"
            whistleblower "Let's start with Julian and see where the trail leads."
            jump julian_scenario

label ethan_sceario:

    scene council_office_day with fade
    whistleblower "You decide to focus on Ethan first. As a council member known for his outspoken criticism, he seems like a potential suspect."
    narrator "You find Ethan in his office, reviewing documents. He looks up and greets you with a neutral expression."

    menu:
        "Did you have access to the draft?":
            suspect7 "Of course I had access to it. As a council member, it’s part of my job to review such documents."
            narrator "Ethan's response is straightforward, but his calm demeanor gives little away."
        "Why would you leak the draft?":
            suspect7 "Leak it? I may not agree with the leadership, but I wouldn't stoop to such tactics. I prefer to fight my battles openly."
            narrator "Ethan's answer seems genuine, but his reputation as a dissenter keeps him under suspicion."
        "Did you notice anything unusual recently?":
            suspect7 "I did notice Julian acting nervous after a recent meeting. He was fumbling with his bag, like he was trying to hide something."
            narrator "Ethan’s observation about Julian raises your curiosity."

    narrator "As you leave Ethan’s office, you notice a sticky note on his desk with a cryptic reminder: 'Meet J at 3 PM.'"
    narrator "You make a mental note to investigate further and decide to question Lila next."

    jump lila_investigation

label lila_investigation:

    scene council_hallway_day with fade
    whistleblower "Next, you decide to question Lila Montgomery. As an intern tasked with managing the draft, she might know more than she’s letting on."
    narrator "You find Lila in the hallway, carrying a stack of files. She looks startled when you approach."

    menu:
        "Did you handle the draft directly?":
            suspect8 "Yes, I was in charge of distributing copies to the council members. I made sure everything was accounted for."
            narrator "Her role in handling the draft puts her in a position of opportunity, but her tone suggests she’s trying to stay professional."
        "Did anyone pressure you about the draft?":
            suspect8 "No, not at all. Everyone was respectful. I didn’t feel any undue pressure."
            narrator "Lila’s answer is measured, but her hesitation raises a red flag."
        "Did you see anything suspicious?":
            suspect8 "I did see Julian staying late in the office the night before the leak. He was printing something, but I didn’t think much of it."
            narrator "Her comment about Julian corroborates Ethan’s earlier observation."

    narrator "As Lila hurries off to her next task, you notice a stray printout in the recycling bin nearby. It’s a partial copy of the draft with Julian’s initials scribbled in the corner."
    narrator "You decide to investigate Julian next."

    jump julian_investigation

label julian_investigation:

    scene council_archive_room with fade
    whistleblower "Finally, you confront Julian in the archive room. He’s busy organizing files but looks up nervously when you enter."
    narrator "Julian fidgets with his glasses, avoiding eye contact."

    menu:
        "Did you handle the draft directly?":
            suspect9 "No, my job is just to organize the documents. I don’t usually handle council drafts."
            narrator "His response is overly defensive, making you suspicious."
        "Why were you printing documents late at night?":
            suspect9 "I... I wasn’t printing anything! You must have the wrong person."
            narrator "Julian’s denial doesn’t match Lila’s observation, deepening your suspicion."
        "Why are your initials on this printout?":
            suspect9 "I... I must have been reviewing it for formatting errors. It’s part of my job to ensure consistency."
            narrator "His explanation is weak, and his nervous tone suggests he’s hiding something."

    narrator "With Julian’s confession, the case is solved, and you prepare your report for the council."

    jump final_scene

label lila_scenario:

    scene council_hallway_day with fade
    whistleblower "You decide to start your investigation with Lila Montgomery. As the intern who managed the draft, she seems like a plausible suspect."
    narrator "You find Lila in the hallway, carrying a stack of files. She looks startled when you approach."

    menu:
        "Did you handle the draft directly?":
            suspect8 "Yes, I was in charge of distributing copies to the council members. I made sure everything was accounted for."
            narrator "Her role puts her in a position of opportunity, but her tone suggests she’s trying to stay professional."
        "Did anyone pressure you about the draft?":
            suspect8 "No, not really. Everyone was polite, though Ethan did ask me some odd questions about it once."
            narrator "Her mention of Ethan piques your interest."
        "Did you see anything unusual the night before the leak?":
            suspect8 "I saw Julian staying late in the office. He was printing something, but I didn’t think much of it."
            narrator "Her comment about Julian raises your suspicion."

    narrator "As Lila hurries off to her next task, you notice a sticky note sticking out of her organizer. It says: 'E. asked for early access. Do not tell anyone.'"
    narrator "You decide to investigate Julian next."

    jump julian_investigation_lila

label julian_investigation_lila:

    scene council_archive_room with fade
    whistleblower "Next, you decide to question Julian Sterling. His late-night printing session might hold clues about the leak."
    narrator "You find Julian in the archive room, shuffling through documents. He looks up nervously when you approach."

    menu:
        "Did you stay late in the office the night before the leak?":
            suspect9 "Yes, but only to catch up on work! I wasn’t doing anything suspicious."
            narrator "His response is defensive, making you more curious."
        "Why were you printing documents late at night?":
            suspect9 "Okay, fine! Ethan asked me to review the draft for him. He said it was for council purposes, so I didn’t question it."
            narrator "Julian’s admission implicates Ethan, but he might still have been involved."
        "Did you notice anything strange while working?":
            suspect9 "Lila looked stressed. I heard her muttering about someone pressuring her, but I didn’t catch the details."
            narrator "His comment aligns with Lila’s earlier mention of Ethan’s odd questions."

    narrator "Before leaving, you notice a crumpled piece of paper in Julian’s trash bin. It’s part of the leaked draft with Ethan’s handwriting in the margins."
    narrator "Armed with this new evidence, you decide to confront Ethan."

    jump ethan_confrontation

label ethan_confrontation:

    scene council_office_day with fade
    whistleblower "You decide to confront Ethan about the evidence tying him to the leak."
    narrator "You find Ethan in his office, calmly reviewing documents. He looks up with a faint smile."

    menu:
        "Why is your handwriting on this draft?":
            suspect7 "I was simply reviewing it! That’s part of my job as a council member."
            narrator "Ethan’s calm demeanor falters slightly as he speaks."
        "Why did you pressure Julian and Lila?":
            suspect7 "Pressure? I didn’t pressure anyone! I asked for help with reviewing the draft, that’s all."
            narrator "His tone grows defensive, and you sense he’s hiding something."
        "Did you leak the draft?":
            suspect7 "What? Of course not! I might not agree with the council’s decisions, but leaking documents isn’t how I operate."
            narrator "Ethan’s denial is firm, but the mounting evidence suggests otherwise."

    narrator "As you press Ethan further, cracks start to show in his story. Finally, he snaps under the pressure and confesses."

    suspect7 "Fine! I leaked the draft! The public deserved to know how the council is planning to gut essential programs."
    suspect7 "I didn’t do it for personal gain—I did it for the community."

    narrator "Ethan’s confession reveals his motive. While his intentions might have been noble, his actions caused widespread chaos."
    narrator "You inform the council about your findings, and Ethan is held accountable for his actions."

    jump final_case_resolved_ethan

label final_case_resolved_ethan:

    scene council_hall_day with fade
    whistleblower "Ethan has been identified as the source of the leak. While his actions were well-intentioned, they caused significant damage."
    whistleblower "The council can now begin repairing its relationship with the community."
    whistleblower "Excellent work, Alex. Are you ready for the next challenge?"

    menu:
        "Proceed to the Next Case":
            jump final_scene
        "End Game":
            return

    return

label julian_scenario:

    scene council_archive_room with fade
    whistleblower "You decide to focus your initial investigation on Julian Sterling. As the administrative officer responsible for council documents, he had access to the draft."
    narrator "You find Julian in the archive room, organizing files. He looks up nervously as you approach."

    menu:
        "Did you handle the draft directly?":
            suspect9 "No, I don’t usually deal with drafts. My role is more about filing and document organization."
            narrator "His answer seems evasive, considering his position."
        "Why were you printing documents late at night?":
            suspect9 "I wasn’t printing anything suspicious! I stayed late to catch up on work—end of story."
            narrator "Julian’s response doesn’t match what others have said about his activities that night."
        "Do you know anything about the leak?":
            suspect9 "Nothing at all! I was as surprised as anyone when I heard about it."
            narrator "Julian’s nervous demeanor and defensive tone make you suspect he’s hiding something."

    narrator "Before leaving, you notice a crumpled piece of paper in Julian’s trash bin. It’s part of the leaked draft, with faint ink smudges that match the official council stationery."
    narrator "You decide to investigate Ethan Banks next to cross-check Julian’s claims."

    jump ethan_investigation_julian

label ethan_investigation_julian:

    scene council_office_day with fade
    whistleblower "You decide to question Ethan Banks next. As a vocal critic of the council, he might have had a motive to leak the draft."
    narrator "Ethan is in his office, reviewing documents. He looks up and greets you with a neutral expression."

    menu:
        "Did you review the draft?":
            suspect7 "Of course I did. It’s part of my job as a council member. But I didn’t leak it, if that’s what you’re implying."
            narrator "Ethan’s response is straightforward, but his calm demeanor gives little away."
        "Why did you ask Julian to review the draft?":
            suspect7 "I didn’t ask Julian to review it—I simply handed it to him for formatting checks. He’s better with that stuff than I am."
            narrator "Ethan’s statement contradicts Julian’s earlier denial about handling the draft."
        "Did you notice anything unusual recently?":
            suspect7 "Yes. Lila seemed unusually stressed during the last meeting. She was fidgeting a lot, like she was hiding something."
            narrator "Ethan’s observation about Lila adds a new layer to the investigation."

    narrator "As you leave Ethan’s office, you notice a sticky note on his desk with a cryptic reminder: 'Follow up with Lila.'"
    narrator "You decide to question Lila next."

    jump lila_investigation_julian

label lila_investigation_julian:

    scene council_hallway_day with fade
    whistleblower "Next, you decide to question Lila Montgomery. As the intern who managed the draft, she had direct access and opportunity."
    narrator "You find Lila in the hallway, carrying a stack of files. She looks startled when you approach."

    menu:
        "Did you handle the draft directly?":
            suspect8 "Yes, I was responsible for distributing the copies to the council members. I made sure everything was accounted for."
            narrator "Her role puts her in a position of opportunity, but her tone suggests she’s trying to stay professional."
        "Did anyone pressure you about the draft?":
            suspect8 "No, not really. Julian did ask me about the distribution process, but it seemed like a routine question."
            narrator "Her mention of Julian aligns with Ethan’s earlier claim."
        "Did you see anything unusual the night before the leak?":
            suspect8 "I saw Julian staying late in the office, printing something. I didn’t think much of it at the time."
            narrator "Lila’s attempt to redirect suspicion to Julian feels calculated."

    narrator "As Lila walks away, you notice a small folded note sticking out of her file folder. It reads: 'Destroy evidence by 8 AM.'"
    narrator "You decide to confront Julian about Lila’s claim and see if he can shed more light."

    jump julian_confrontation

label julian_confrontation:

    scene council_archive_room with fade
    whistleblower "You return to Julian, armed with Lila’s statement and the evidence you’ve gathered."
    narrator "Julian looks increasingly anxious as you begin questioning him."

    menu:
        "Why did Lila see you printing documents late at night?":
            suspect9 "Alright, fine! I was printing something, but it wasn’t the draft. I was working on my personal files."
            narrator "Julian’s excuse seems flimsy, but his tone suggests he’s hiding something bigger."
        "Did you pressure Lila about the draft?":
            suspect9 "No! If anything, she’s the one who seemed overly concerned about the draft’s security."
            narrator "Julian’s claim shifts suspicion back to Lila."
        "Why was part of the leaked draft in your trash?":
            suspect9 "I was reviewing it for formatting issues, like Ethan said. I didn’t leak it—I swear!"
            narrator "Julian’s nervousness doesn’t help his case, but his explanation seems plausible."

    narrator "As Julian pleads his innocence, you realize that the strongest evidence points back to Lila. It’s time to confront her."

    jump lila_confrontation

label lila_confrontation:

    scene council_hallway_day with fade
    whistleblower "With mounting evidence against Lila, you decide to confront her directly."
    narrator "You find Lila in the hallway again, her face pale as you approach."

    menu:
        "Why was there a note about destroying evidence in your folder?":
            suspect8 "I... I don’t know what you’re talking about! That must have been a mistake."
            narrator "Lila’s denial is weak, and her hands are trembling."
        "Did you leak the draft?":
            suspect8 "No! Why would I do that? It would ruin my career!"
            narrator "Her response is defensive, but her panicked tone betrays her guilt."
        "Why did you blame Julian?":
            suspect8 "Because he’s always snooping around! I thought he’d take the fall if anything went wrong."
            narrator "Lila’s admission reveals her attempt to frame Julian."

    narrator "As you press further, Lila finally breaks down and confesses."

    suspect8 "Alright, I admit it! I leaked the draft. I thought the public deserved to know what was being planned."
    suspect8 "But I didn’t want to take the blame—I didn’t think it would cause this much chaos."

    narrator "Lila’s confession leaves no doubt about her guilt. You quickly inform the council of your findings."

    jump final_case_resolved_lila

label final_case_resolved_lila:

    scene council_hall_day with fade
    whistleblower "Lila has been identified as the source of the leak. While her intentions might have been noble, her actions caused significant damage."
    whistleblower "The council can now begin repairing its relationship with the community."
    whistleblower "Excellent work, Alex. Another mystery solved. Are you ready for the next challenge?"

    menu:
        "Proceed to the Next Case":
            jump final_scene
        "End Game":
            return

    return

    
label final_scene:

    scene council_hall_day with fade
    whistleblower "The truth is revealed, and the council can now address the situation transparently."
    whistleblower "Well done, Alex. Another mystery solved. Are you ready for the next challenge?"

    menu:
        "Proceed to the Next Case":
            jump next_case
        "End Game":
            return

    return
