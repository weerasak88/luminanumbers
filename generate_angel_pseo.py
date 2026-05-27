"""
Lumina Numbers — Angel Number pSEO Generator
สร้าง: /angel-number-[n]/ (24 หน้า)
อัปเดต: sitemap.xml
รัน: python generate_angel_pseo.py
"""

import os

BASE = r"C:\zkambheer\luminanumbers"
GA_ID = "G-LSCWW3E9XV"

# ─── Full Data ───────────────────────────────────────────
DATA = {
  111: {
    "title": "Accelerated Manifestation and Initiation",
    "h1": "Unlocking the Spiritual Significance and Meaning of Angel Number 111",
    "meta": "Discover the profound symbolism of angel number 111. Explore its powerful implications for romantic love, career trajectory, financial success, and twin flames.",
    "crystal": "Clear Quartz",
    "frequency": "Very Common",
    "color": "#c9a96e",
    "intro": "The numeric sequence 111 operates as a profound energetic catalyst within numerological frameworks. Rooted entirely in the foundational digit one, which universally symbolizes creation, absolute independence, and laser-focused intention, this repeating sequence serves as a metaphysical alarm clock for the observer. In astrological contexts, this energy correlates intimately with the first house of the zodiac, governing self-expression, identity, and the courage to exist authentically. It mirrors the archetype of The Magician in the major arcana of the tarot, representing the master manifestor who utilizes all available elemental tools to shape the material realm.",
    "why": "When an individual repeatedly questions the appearance of 111, the answer lies in the psychological and spiritual mechanics of manifestation. The universe functions as an expansive mirror, reflecting the individual's dominant mental state back to them through synchronistic events. Spotting this number on clocks or documents is interpreted as a cosmic confirmation that current trajectories are perfectly aligned with higher purposes. It serves as a gentle yet urgent reminder to monitor cognitive patterns closely and to decisively set clear intentions for the future.",
    "general": "The sequence 111 functions as a powerful wake-up call signaling that your thoughts are rapidly manifesting into reality. It represents the initiation of new beginnings and a sudden opening of energetic portals. You are urged to maintain a highly positive and focused mindset to shape a favorable future.",
    "love": "This number indicates that fresh romantic opportunities are manifesting quickly in your immediate environment. It encourages you to stay optimistic and be exceptionally clear about the traits you desire in a partner. For those in relationships, it calls for authentic expression of personal truth without fear of disruption.",
    "career": "New professional chapters and sudden leadership opportunities are emerging rapidly. Focus on your ultimate vocational ambitions and take independent initiative rather than dwelling on current limitations. This is an optimal period for entrepreneurs to launch businesses and for professionals to pitch groundbreaking ideas.",
    "finance": "A rapid surge of financial potential is available if you align your mindset with pure abundance. Trust that novel income streams are currently being generated through your positive intentions. Maintaining a constructive and optimistic outlook regarding material resources is crucial at this time.",
    "twin_flame": "You are energetically aligning with your twin flame through the elevation of your highest thoughts. Maintain a high vibrational frequency to draw this profound soul connection closer into physical reality. The sequence 111 emphasizes that finding lasting unity first requires profound independence and a complete sense of self.",
    "action": "Pause immediately to monitor your current thoughts, deliberately shifting your focus away from fear and solely toward what you desire to create."
  },
  222: {
    "title": "Equilibrium and Divine Trust",
    "h1": "Angel Number 222: The Path to Balance, Harmony, and Relational Alignment",
    "meta": "Uncover the harmonizing power of angel number 222. Learn how this sequence influences romantic relationships, career growth, financial stability, and twin flames.",
    "crystal": "Rose Quartz",
    "frequency": "Very Common",
    "color": "#b8d4e8",
    "intro": "The repeating sequence 222 resonates with the gentle frequencies of diplomacy, cooperation, and profound relational harmony. In esoteric traditions, the number two is universally recognized as the digit of partnership and duality, representing the delicate balance required to sustain both internal peace and external connections. When amplified threefold, the sequence acts as a powerful energetic stabilizer, encouraging a departure from aggressive energy and shifting focus toward patience, steady progress, and the cultivation of deep trust in the unfolding cosmic process.",
    "why": "The continuous observation of 222 generally occurs during periods of internal friction or interpersonal tension, signaling an urgent need to restore equilibrium across various life domains. It frequently appears when an individual has been overworking at the direct expense of their emotional well-being. Seeing 222 is a clear directive to cease rushing, trust that the foundational work is yielding unseen results, and allow complex situations to naturally harmonize over time.",
    "general": "The number 222 carries a gentle frequency of balance, emotional healing, and deep reassurance from the universe. It acts as a reminder that everything is aligning perfectly behind the scenes, even if progress appears stagnant. You are being asked to release urgency and cultivate profound trust in divine timing.",
    "love": "This sequence represents emotional alignment, mutual cooperation, and the restoration of harmony within relationships. It encourages patience and open communication, reminding you that true love develops steadily and naturally. The strongest relationships require significant time to build; therefore, patience, grace, and mutual trust are paramount.",
    "career": "Your professional efforts are quietly taking root, requiring you to maintain steady cooperation with colleagues. Avoid impulsive career moves and trust that your current trajectory is correct and will yield results soon. The number emphasizes that shared victories will yield far more profound long-term benefits than isolated achievements.",
    "finance": "Financial stability is being established through a balanced and patient approach to wealth management. It advises against extreme financial risks, promoting a steady, harmonious cultivation of resources. Trust the long-term process and allow compound growth to mature organically.",
    "twin_flame": "Your twin flame journey is entering a phase of crucial emotional balancing and mutual healing. Patience is paramount as both souls undergo the necessary alignment to sustain a harmonious eventual union. The sequence confirms that beneath the surface turbulence, the foundational energies of the two souls are actively working toward alignment.",
    "action": "Slow down, regulate your emotional state, and practice patience by trusting that your current path is unfolding exactly as it should."
  },
  333: {
    "title": "Creative Expression and Ascended Guidance",
    "h1": "Embracing the Creative and Communicative Power of Angel Number 333",
    "meta": "Explore the vibrant energy of angel number 333. Learn how this sequence amplifies creativity, enhances love, boosts career prospects, and aligns twin flames.",
    "crystal": "Carnelian",
    "frequency": "Very Common",
    "color": "#e8d070",
    "intro": "The sequence 333 vibrates with the dynamic, highly charged frequencies of creativity, uninhibited self-expression, and the complete alignment of mind, body, and soul. In numerological theory, the number three represents the socialite — the energetic force that thrives on connection, artistic output, and joyful expansion. Astrologically, it aligns seamlessly with the third house of the zodiac, which directly governs communication, intellectual curiosity, and local mobility. It also mirrors the abundant, fertile energy of The Empress in the traditional tarot deck.",
    "why": "When an individual continuously observes the sequence 333, it typically functions as a cosmic wakeup call to abandon isolation, step out of the shadows, and engage more fully with the external world. The appearance of this pattern strongly suggests that the observer has been harboring brilliant creative ideas, unexpressed emotions, or a deep desire for broader social connection that must now be actualized. The universe is indicating that the individual is surrounded by invisible spiritual support.",
    "general": "The sequence 333 is a vibrant call to access your innate creativity and achieve harmony across your mind, body, and spirit. It signifies the supportive presence of Ascended Masters who are guiding your personal expansion. You are encouraged to express your authentic self boldly and without hesitation.",
    "love": "This number demands open, honest communication to deepen romantic bonds and clear up any lingering misunderstandings. For single individuals, it signals that adopting a socially active and optimistic demeanor will attract true love. The sequence urges playful interaction, high-level intellectual stimulation, and the injection of pure joy into the relational dynamic.",
    "career": "Your professional life requires an injection of creativity, collaboration, and clear articulation of your innovative ideas. It is an ideal time to step into the spotlight and confidently pitch new projects to leadership. The sequence is highly favorable for individuals operating in creative, communicative, or media-driven industries.",
    "finance": "Financial abundance is closely tied to your ability to monetize your unique creative passions and communicate your value. It warns against material hoarding, suggesting that wealth flows best when shared and enjoyed. Financial growth is inextricably linked to the observer's ability to seamlessly collaborate with others.",
    "twin_flame": "This sequence points toward an imminent encounter or a significant breakthrough in communication with your twin flame. It urges both individuals to express their deepest spiritual truths to foster an unbreakable bond. The sequence represents the holy trinity of alignment: the harmonization of the two individuals with their higher divine purpose.",
    "action": "Engage in a creative project, speak your truth confidently, and actively expand your social connections."
  },
  444: {
    "title": "Angelic Protection and Solid Foundations",
    "h1": "Angel Number 444: Building Foundations and Securing Spiritual Protection",
    "meta": "Discover the grounding energy of angel number 444. Learn how this powerful sequence influences stability in love, career development, wealth, and twin flames.",
    "crystal": "Black Tourmaline",
    "frequency": "Very Common",
    "color": "#8899aa",
    "intro": "The sequence 444 acts as the architectural blueprint of the numerological realm, radiating heavy frequencies of immense stability, structural integrity, and diligent, unglamorous effort. The number four is intrinsically linked to the concept of the home base, representing the four cardinal directions, the four elements, and the solid foundation required to support any lasting earthly endeavor. When amplified as 444, the sequence serves as an undeniable confirmation of spiritual protection, indicating that the observer's physical and energetic environments are being heavily guarded by higher angelic forces.",
    "why": "The repeated appearance of 444 frequently occurs when an individual is in the grueling process of building something significant — be it a demanding career, a family unit, or a completely new lifestyle — and requires deep reassurance that their systematic efforts are not in vain. It serves as a stark reminder to honor the physical body as the soul's permanent home on earth. Furthermore, encountering 444 is a clear signal to aggressively purge the immediate environment of toxic stress and highly unreliable acquaintances.",
    "general": "The sequence 444 is a profound indicator of intense angelic protection and the grounding of your personal energy. It confirms that you are surrounded by divine support as you work diligently toward your long-term objectives. The universe is urging you to focus on building stable, enduring foundations for your future.",
    "love": "This number emphasizes the creation of a secure, loyal, and practically grounded romantic partnership. It suggests that enduring love requires consistent effort, mutual protection, and a shared commitment to building a life together. The number also demands intense intuitive scrutiny of the broader social circle.",
    "career": "Your dedication and disciplined work ethic are being recognized, leading to solid career progression. It is a reminder to remain organized, persistent, and focused on the structural integrity of your professional projects. Lasting success will be achieved strictly through relentless consistency, discipline, and a focus on long-term structural integrity.",
    "finance": "Financial security is achievable through meticulous planning, budgeting, and the steady accumulation of wealth over time. Avoid get-rich-quick schemes and focus on investments that provide long-term material stability. The sequence guarantees that hard work and a steady approach to saving are currently working and will eventually yield massive dividends.",
    "twin_flame": "Your twin flame connection is being spiritually safeguarded against external negative influences. The relationship requires both partners to focus on creating a grounded, emotionally safe environment for mutual growth. The sequence provides profound, grounding reassurance during the often-turbulent phases of the connection.",
    "action": "Ground your energy, commit to disciplined action, and trust that you are completely protected by divine forces."
  },
  555: {
    "title": "Dynamic Transformation and Unrestricted Freedom",
    "h1": "Angel Number 555: Navigating Radical Transformation and Personal Freedom",
    "meta": "Embrace the winds of change with angel number 555. Understand its profound impact on romantic transitions, career shifts, financial opportunities, and twin flames.",
    "crystal": "Labradorite",
    "frequency": "Common",
    "color": "#70c8b0",
    "intro": "The sequence 555 is the numerological harbinger of profound, sweeping, and often unexpected transformation. In direct contrast to the stabilizing energy of the number four, the digit five embodies relentless motion, high adaptability, and the pursuit of absolute personal freedom. When encountering 555, the observer is being formally placed on notice that the static, predictable elements of their life are about to undergo a radical restructuring. This sequence represents the energetic pivot point where outdated structures are dismantled to make way for unprecedented personal expansion.",
    "why": "When an individual asks 'Why am I seeing 555?', the analytical conclusion is that a major paradigm shift is imminent on their personal timeline. This sequence appears when the soul has outgrown its current container, necessitating a disruption of comfortable yet limiting routines. The universe presents 555 to advise the observer to remain highly flexible, to surrender control, and to release any rigid attachments to specific outcomes. These disruptions are meticulously orchestrated cosmic events designed to align the individual more closely with their ultimate evolutionary trajectory.",
    "general": "The sequence 555 announces that massive, unavoidable transformations are currently unfolding or are imminent in your life. It is a divine signal to completely release outdated patterns and eagerly welcome the unknown. Embracing extreme adaptability will ensure these major life shifts lead to your ultimate liberation.",
    "love": "Significant evolutionary changes are occurring within your romantic life, which may involve deep rejuvenation or the necessary ending of a stagnant dynamic. You must remain emotionally flexible and open to entirely new experiences in love. For singles, it indicates that a sudden, highly unexpected encounter may entirely alter their romantic landscape.",
    "career": "Expect sudden shifts in your professional trajectory, such as a major role change, a new job, or an unexpected entrepreneurial opportunity. These career disruptions are purposefully designed to align you with your true vocational calling. By remaining highly adaptable and trusting your innate abilities to navigate new waters, you will discover roles that offer greater autonomy.",
    "finance": "Your financial situation is undergoing a transition that requires you to adapt your earning and spending strategies rapidly. Embrace innovative financial opportunities and be willing to take calculated risks for greater monetary freedom. The sequence warns strongly against financial rigidity during this transit.",
    "twin_flame": "The twin flame dynamic is experiencing a period of intense, rapid evolution that requires both souls to shed old karmic baggage. Embrace the ensuing changes, as they are essential for moving the connection to a higher operational frequency. The twins must rapidly adapt to higher frequencies of unconditional love.",
    "action": "Let go of all resistance, remain highly adaptable, and proactively embrace the incoming life changes with absolute optimism."
  },
  666: {
    "title": "Radical Self-Love and Holistic Balance",
    "h1": "Demystifying Angel Number 666: The Call for Earthly Balance and Healing",
    "meta": "Look beyond the myths of angel number 666. Discover its true meaning related to emotional balance, self-care, career realignment, and twin flame healing.",
    "crystal": "Rhodochrosite",
    "frequency": "Rare",
    "color": "#f0a0b8",
    "intro": "Despite centuries of intense cultural stigmatization, the numeric sequence 666 holds a profoundly nurturing, restorative, and grounding significance within genuine esoteric and numerological frameworks. The base digit six is universally associated with domestic harmony, deep emotional responsibility, and the cultivation of unconditional love. When amplified as 666, the sequence serves not as a harbinger of doom, but as a critical, loving intervention from higher realms urging the observer to find immediate balance. It is a gentle yet firm prompt to realign life with true internal values.",
    "why": "The persistent observation of 666 almost universally occurs when an individual's life has become severely skewed toward external pressures — such as obsessive career ambition, financial panic, or the hoarding of material possessions — at the direct expense of their mental and emotional well-being. The universe utilizes this sequence to halt the individual's current destructive trajectory, demanding a profound reassessment of priorities. It is a call to practice radical self-care, stop ignoring the physical signs of burnout, and re-establish a spiritual center.",
    "general": "Contrary to popular myth, 666 is a deeply compassionate sequence urging you to restore harmony between your material pursuits and spiritual health. It indicates that your thoughts may be out of balance, driven excessively by fear or worldly anxieties. You are being called to return to a state of profound self-love and internal peace.",
    "love": "This number highlights the necessity of healing internal emotional wounds to prevent projecting insecurities onto your romantic partner. True relational harmony can only be achieved when you first offer unconditional love and acceptance to yourself. For single individuals, the sequence indicates a strict requirement to heal lingering trauma before forging new connections.",
    "career": "You are heavily cautioned against allowing professional ambition to completely consume your identity and personal life. Reassess your work-life balance immediately to ensure your career serves your well-being rather than destroying it. It is an optimal time to establish strict boundaries and find intrinsic joy in the daily execution of tasks.",
    "finance": "Financial anxieties are currently blocking your natural flow of abundance, requiring a shift away from a scarcity mindset. Trust in divine provision and focus on ethical, balanced wealth generation rather than desperate accumulation. Financial stability is best achieved when decisions are made calmly and from a place of sufficiency.",
    "twin_flame": "This sequence frequently appears during painful twin flame separations, serving as a directive to heal individual childhood traumas and codependency. The separation is a purposeful phase meant to correct imbalances before a harmonious reunion can occur. The observer must redirect immense energy inward to heal themselves first.",
    "action": "Audit your life for imbalances, release material anxieties, and aggressively prioritize your emotional and spiritual self-care."
  },
  777: {
    "title": "Profound Spiritual Enlightenment",
    "h1": "The Ultimate Confirmation: Decoding the Luck and Alignment of Angel Number 777",
    "meta": "Explore the mystical energy of angel number 777. Understand why this sequence acts as the ultimate confirmation of spiritual alignment, love, and wealth.",
    "crystal": "Amethyst",
    "frequency": "Rare",
    "color": "#9b6bbf",
    "intro": "The numeric sequence 777 occupies a unique, highly exalted position within the spectrum of angelic patterns. In numerology, the number seven is inextricably linked to deep inner wisdom, spiritual completeness, and perfect alignment with the divine will. Unlike other repeating numbers that function as warnings or course corrections, 777 is a number of pure, unadulterated confirmation. It appears only when the internal psychological landscape and the external material reality have finally harmonized into a state of supreme flow.",
    "why": "When an individual questions the sudden ubiquity of 777, the analytical deduction is remarkably straightforward: the grueling hard work has already been completed. The universe does not deploy this specific sequence to encourage those who are faltering or off-path; it deploys it exclusively as a reward for those who have consistently made difficult, spiritually aligned choices over a sustained period. The appearance of 777 confirms that the individual is in an active flow state and major, positive expansions are already materializing.",
    "general": "The sequence 777 is a highly auspicious indicator of deep spiritual growth, enlightenment, and alignment with the higher realms. It confirms that you are successfully navigating your spiritual journey and trusting your inner intuition accurately. The universe is celebrating your expansion in consciousness and inner wisdom.",
    "love": "Your romantic connections are evolving beyond the superficial, requiring a partner who can meet you on an intensely spiritual level. It encourages you to trust your intuitive feelings regarding the energetic compatibility of your relationships. This sequence indicates that the partnership has successfully navigated previous difficulties and emerged as a deeply honest, spiritually significant union.",
    "career": "Professional success will be achieved by aligning your career choices strictly with your higher spiritual purpose and ethics. You are encouraged to utilize your profound inner wisdom to guide your vocational trajectory. The sequence provides one of the strongest possible confirmations that the current career path is correct and highly favored by universal forces.",
    "finance": "Financial rewards are manifesting as a direct result of your spiritual alignment and ethical handling of resources. Maintain your faith in the universe, as spiritual richness is currently translating into material prosperity. The sequence indicates that the observer is closer to financial stability than they realize.",
    "twin_flame": "The twin flame connection is reaching an unprecedented depth of spiritual telepathy and mutual energetic recognition. Both individuals are experiencing simultaneous spiritual awakenings that draw their souls irrevocably closer. The sequence signals that the relationship is officially transitioning out of its volatile phases and moving into a harmonious period.",
    "action": "Deepen your meditation practices, trust your intuitive faculties implicitly, and continue your pursuit of esoteric knowledge."
  },
  888: {
    "title": "Infinite Abundance and Karmic Reward",
    "h1": "Mastering Abundance: The Infinite Rewards of Angel Number 888",
    "meta": "Discover the powerful wealth and success associated with angel number 888. Learn how this sequence influences financial prosperity, career, and twin flames.",
    "crystal": "Citrine",
    "frequency": "Rare",
    "color": "#c9a96e",
    "intro": "The repeating sequence 888 operates as the ultimate numerological symbol of material mastery, financial abundance, and the continuous, unbroken flow of energetic exchange. Visually representing the infinity symbol turned upright, the number eight is fundamentally connected to the universal law of cause and effect, highlighting the absolute balancing of karmic scales. When this digit is amplified threefold, it signifies that the observer has entered a highly favorable phase where past efforts, investments, and positive actions are yielding massive, tangible returns.",
    "why": "The repeated appearance of 888 serves to directly notify the individual that they are perfectly in line with their destiny and have successfully tapped into an infinite stream of universal abundance. This sequence generally manifests when a long, arduous cycle of labor, discipline, or spiritual growth is finally reaching its harvest period. The universe utilizes this number to confirm that the observer's dedicated efforts have not gone unnoticed and that significant rewards await.",
    "general": "The sequence 888 is a powerful omen of infinite abundance, immense success, and the arrival of well-deserved karmic rewards. It signifies that your past efforts have generated a continuous flow of prosperity that is now entering your physical reality. You are fully supported by the universe in mastering the material and spiritual realms simultaneously.",
    "love": "Your love life is entering a phase of rich emotional abundance and deeply reciprocal exchange. It indicates that the love you have selflessly given in the past is returning to you multiplied through a fulfilling partnership. The sequence often points to a partnership where both individuals share similar high-level ambitions and drive.",
    "career": "You are reaching the absolute pinnacle of professional achievement, marked by significant recognition and career mastery. This is a highly favorable time to request promotions, close major deals, or expand your business operations. The sequence signifies major professional advancement and the attainment of high-level leadership positions.",
    "finance": "An extraordinary financial windfall or the establishment of a highly lucrative income stream is currently manifesting. You are encouraged to graciously accept this wealth and utilize it to further expand your influence and generosity. The sequence is an undeniable, powerful signal of incoming wealth and absolute monetary abundance.",
    "twin_flame": "The twin flame relationship is characterized by an infinite, circulating flow of perfectly balanced energy between both partners. The union will act as a powerful catalyst for generating shared abundance and fulfilling your joint earthly mission. The intense karmic debts often associated with twin flame dynamics have been largely balanced.",
    "action": "Open yourself completely to receiving wealth, celebrate your success, and ensure your energy remains in a state of generous flow."
  },
  999: {
    "title": "Karmic Completion and Soul Renewal",
    "h1": "Angel Number 999: The Completion of Cycles and Humanitarian Awakening",
    "meta": "Understand the transformative power of angel number 999. Discover what this sequence means for life cycles, career transitions, love, and twin flame unions.",
    "crystal": "Selenite",
    "frequency": "Rare",
    "color": "#c84848",
    "intro": "The numeric sequence 999 represents the precipice of profound transformation, serving as the numerological symbol for the absolute completion of a major life cycle. As the final single digit in numerology, the number nine embodies the culmination of all preceding lessons, radiating frequencies of enlightenment, deep inner wisdom, and global humanitarianism. When amplified threefold, the sequence acts as a cosmic signal that a specific chapter in the observer's life has fulfilled its karmic purpose and must be definitively concluded to make space for unprecedented new beginnings.",
    "why": "When an individual encounters the repeated sequence 999, it is a direct universal directive to engage in the incredibly difficult process of letting go. The observer is being notified that clinging to situations, people, or environments that no longer serve their highest good will only result in severe energetic stagnation. Furthermore, 999 serves as a prompt to shift focus from hyper-individualistic desires toward a broader, more humanitarian perspective, using acquired wisdom to assist others.",
    "general": "The sequence 999 represents the definitive conclusion of a major life chapter and the clearing of old karmic cycles. It is a powerful sign of spiritual graduation, urging you to release obsolete patterns and identities. By surrendering to these natural endings, you prepare your soul for a massive energetic renewal.",
    "love": "A romantic relationship may be reaching its natural conclusion, or an outdated dynamic within an existing partnership must be entirely dismantled. You are required to forgive past hurts and release attachments to make space for a higher frequency of love. For those in healthy partnerships, 999 indicates the end of one phase and the rapid beginning of a deeper commitment.",
    "career": "Your current professional path has taught you everything it can, signaling that it is time to transition toward your true life purpose. Do not fear leaving behind a secure but unfulfilling job, as a more aligned vocation awaits. The sequence heralds a period of significant, often total professional transition.",
    "finance": "Financial obligations, debts, or old methods of earning are coming to a definitive close, allowing for a fresh economic start. Focus your resources on humanitarian or spiritually fulfilling endeavors rather than pure accumulation. It is time to definitively end poor financial practices and aggressively pay off lingering debts.",
    "twin_flame": "A difficult phase of the twin flame journey is ending, bringing ultimate closure to past-life karma and deeply entrenched blockages. This profound clearing is the final prerequisite before the souls can ascend to the next level of their shared destiny. The sequence demands that both individuals practice profound patience.",
    "action": "Release all attachments to the past with love, forgive what needs closure, and boldly prepare for a completely new beginning."
  },
  1010: {
    "title": "Divine Orchestration and Infinite Potential",
    "h1": "Angel Number 1010: Divine Orchestration and Infinite Potential Unlocked",
    "meta": "Discover the deep meaning of angel number 1010. Learn how this powerful sequence influences spiritual awakening, love, career, finances, and twin flames.",
    "crystal": "Rose Quartz & Citrine",
    "frequency": "Common",
    "color": "#d4bfe8",
    "intro": "The sequence 1010 acts as a reassuring message that your life is unfolding exactly as envisioned through divine orchestration. By combining the energy of 1 (creation) and 0 (infinite potential and the void), this sequence represents the direct tapping into the universal source code. The presence of 0 amplifies the 1, indicating that the new beginnings occurring are not minor shifts, but rather paradigm-altering events supported by cosmic forces.",
    "why": "The consistent observation of 1010 indicates that the individual is in a phase of profound spiritual completeness and is being called to step forward courageously while simultaneously allowing the universe to handle the intricate details. It appears when the observer must learn that taking initiative and practicing surrender are not mutually exclusive, but rather complementary steps in the delicate dance of manifestation.",
    "general": "The sequence 1010 acts as a reassuring message that your life is unfolding exactly as envisioned through divine orchestration. It whispers promises of spiritual awakening and urges you to embrace the infinite possibilities of the universe. Stepping out of your comfort zone is now mandatory to unlock your highest potential.",
    "love": "This number is a powerful reminder of profound self-love and the achievement of perfect romantic alignment. The universe is actively conspiring to bring you a deep soul connection that resonates with pure joy. The sequence heralds a period of deep intimacy, mutual support, and highly positive shifts in romantic life.",
    "career": "It signifies the initiation of entirely new professional ventures and stepping into visionary leadership roles with absolute confidence. Embracing discomfort and radical change at work is necessary to achieve your ultimate career evolution. Your unique talents are fully aligned with your life purpose, making this an excellent time for bold career moves.",
    "finance": "A massive wave of prosperity is approaching as the universe aligns to usher in unparalleled material abundance. Your positive thoughts and structured actions are actively attracting immense, sustainable financial growth. The sequence is a harbinger of abundance, prosperity, and the rapid materialization of positive intentions.",
    "twin_flame": "This sequence signals a highly harmonious union with your twin flame that has been perfectly orchestrated by divine timing. The connection promises a future filled with deep emotional fulfillment, mutual support, and spiritual elevation. It acts as a definitive sign that the twin flame is drawing closer.",
    "action": "Trust your intuition implicitly and confidently step completely outside your comfort zone to embrace new opportunities."
  },
  1111: {
    "title": "Master Spiritual Awakening",
    "h1": "The Master Number 1111: Spiritual Awakening and Infinite Potential",
    "meta": "Unlock the ultimate spiritual gateway of angel number 1111. Explore its deep ties to lightworkers, instantaneous manifestation, love, and twin flame unions.",
    "crystal": "Clear Quartz",
    "frequency": "Very Common",
    "color": "#a0a8c8",
    "intro": "The numeric sequence 1111 is widely regarded as the most recognizable, potent, and magical pattern within the entire numerological lexicon. It is an amplification of the master number 11, representing a direct, unhindered conduit between the physical, earthly realm and the highest echelons of spiritual consciousness. When the pioneer energy of the number one is quadrupled, it creates a metaphysical threshold — a gateway of infinite potential where the veil between thought and material reality becomes exceptionally thin.",
    "why": "When an individual continuously observes 1111, it signifies that a massive portal of manifestation has opened directly before them. The universe is issuing a high-alert notification that the observer's thoughts, whether positive or negative, are instantly crystallizing into physical reality. Furthermore, seeing 1111 confirms the individual's role as a bridge — a soul capable of holding complex paradoxes and restoring a much-needed sense of oneness and harmony to the world.",
    "general": "The master sequence 1111 signifies an intense spiritual awakening and the opening of a profound energetic portal in your life. It indicates that your thoughts are aligning instantly with universal intelligence to manifest your reality. You are being called to step into your highest potential and true life purpose.",
    "love": "This sequence strongly points toward the manifestation of a highly spiritual, destined soulmate connection. If already partnered, it demands a massive elevation in the spiritual consciousness shared between you. The number outright rejects mundane romance in favor of deep, transformative spiritual merging.",
    "career": "Your career is undergoing a destined evolution that perfectly aligns with your deepest spiritual mission. Trust your visionary ideas and take decisive, pioneering action to forge a completely new professional path. It is an optimal time to launch ventures that have a humanitarian or spiritually uplifting component.",
    "finance": "Your ability to manifest financial abundance is currently operating at absolute maximum capacity. Maintain laser-focused, positive intentions regarding wealth, as the universe is instantly responding to your energetic output. Financial abundance is simply a neutral energy source that can be directed to facilitate profound positive changes.",
    "twin_flame": "1111 is the ultimate twin flame indicator, signaling an imminent encounter, profound spiritual recognition, or a major union milestone. The sequence acts as a magnetic beacon, perfectly aligning the energetic frequencies of both mirror souls. It demands that both twins awaken to their higher calling and move rapidly toward the ultimate goal of harmonious unified spiritual labor.",
    "action": "Set crystal-clear intentions, completely eliminate negative thinking, and step confidently through the new opportunities presenting themselves."
  },
  1122: {
    "title": "Balanced Forward Movement",
    "h1": "Angel Number 1122: Harmonizing Ambition with Inner Peace",
    "meta": "Uncover the meaning of angel number 1122. Discover how this sequence balances ambition with harmony in love, career, finance, and twin flame connections.",
    "crystal": "Opal",
    "frequency": "Rare",
    "color": "#d4bfe8",
    "intro": "The sequence 1122 represents a complex semiotic blending of the pioneering, individualistic energy of the number 1 and the harmonious, cooperative frequency of the number 2. It bridges the gap between self-actualization and interpersonal dependency, facilitating emotional maturity and forward movement through faith. This number frequently appears when a person is standing at a critical juncture, needing to balance their aggressive career ambitions with the preservation of their personal relationships.",
    "why": "The continuous observation of 1122 indicates that the individual is in a phase of profound spiritual completeness and is being called to step forward courageously while simultaneously allowing the universe to handle the intricate details. It appears when the observer must learn that taking initiative and practicing surrender are not mutually exclusive, but rather complementary steps. The universe presents 1122 to confirm that the individual's energetic output is perfectly aligned with their highest purpose.",
    "general": "The sequence 1122 is a powerful message of balanced manifestation, urging you to move forward with unshakeable faith in your journey. It perfectly synthesizes the independent drive for new beginnings with the necessity for inner peace and harmony. You are being supported as you navigate major life changes, provided you maintain emotional equilibrium.",
    "love": "This number demands clear, honest communication and the emotional maturity to heal old relational misunderstandings. True love will grow slowly and naturally if you prioritize balance, mutual effort, and deep emotional understanding. It underscores the reality that balanced, unified energy can only be achieved when both individuals have cultivated inner stability.",
    "career": "Your hard work and disciplined focus are leading directly toward successful career advancement and new opportunities. You must trust your professional path and utilize your leadership strengths while maintaining cooperative partnerships. The sweet spot where independent ambition aligns perfectly with cooperative teamwork is now activated.",
    "finance": "A positive financial mindset combined with consistent, disciplined effort is generating highly stable economic growth. Ensure your daily actions are perfectly aligned with your long-term financial goals to maximize incoming opportunities. The sequence advises a highly balanced approach to wealth: taking decisive steps to generate income while remaining receptive to opportunities the universe provides.",
    "twin_flame": "This sequence indicates significant progress toward reuniting with your twin flame through mutual personal development. It mirrors a balanced partnership where both individuals must be equally present emotionally and spiritually before union is possible. Pay close attention to your intentions and balance personal ambitions with relational harmony.",
    "action": "Pay close attention to your intentions, balance your personal ambitions with relational harmony, and trust the unfolding process."
  },
  1144: {
    "title": "Constructing Divine Reality",
    "h1": "Angel Number 1144: Taking Charge of Your Destiny with Discipline",
    "meta": "Explore the meaning of angel number 1144. Learn how this sequence supports destiny manifestation, relationship growth, career advancement, and twin flames.",
    "crystal": "Black Tourmaline",
    "frequency": "Rare",
    "color": "#8899aa",
    "intro": "Blending the initiation energy of 11 with the extreme structural stability of 44, the sequence 1144 is heavily associated with taking charge of one's reality and building something enduring. From a numerological reduction standpoint, 1+1+4+4 equals 10, which further reduces to 1, bringing the entire sequence back to the core theme of massive new beginnings and self-starting energy. It brings positive energy that acknowledges the alignment of life events with a higher divine plan.",
    "why": "The consistent observation of 1144 is an auspicious sign that you are taking charge of your destiny and manifesting your reality with divine support. It blends the powerful energy of new beginnings with the structured discipline required to build lasting foundations. The universe confirms that your hard work and positive attitude will result in thriving abundance.",
    "general": "The sequence 1144 is an auspicious sign that you are taking charge of your destiny and manifesting your reality with divine support. It blends the powerful energy of new beginnings with the structured discipline required to build lasting foundations. The universe confirms that your hard work and positive attitude will result in thriving abundance.",
    "love": "Exciting changes are occurring in your relationships, urging you to let your true, authentic self flourish. Cultivating deep self-reliance and positive thoughts will prepare you for a highly committed and structurally sound romantic partnership. This sequence calls for a conscious effort to nurture the connection with deep compassion.",
    "career": "A positive shift in a new direction is occurring, requiring you to remain open to unforeseen but highly beneficial career evolutions. Continued dedication to your current projects will soon secure recognition and major advancement from superiors. By maintaining dedication and focusing on the essential elements of your work, you will systematically ascend the professional ladder.",
    "finance": "You are encouraged to make incredibly wise, disciplined financial decisions to establish long-term economic stability. Even if current finances are tight, your perseverance and strategic planning promise complete recovery and future wealth. Wealth will manifest through practical, straightforward actions and by sequentially executing an innovative strategy for long-term prosperity.",
    "twin_flame": "This is a powerful manifestation number indicating imminent progress or a reunion on your complex twin flame journey. It calls for structured emotional growth and the letting go of past negativity to foster a harmonious spiritual bond. The sequence highlights the necessity of healing core vulnerabilities common to twin flames.",
    "action": "Maintain an aggressively positive attitude, focus diligently on your goals, and build strong practical foundations for your future."
  },
  1155: {
    "title": "Transformational Leadership",
    "h1": "Angel Number 1155: Embracing Paradigm Shifts and Bold Leadership",
    "meta": "Understand the meaning of angel number 1155. Learn how this sequence calls for transformational leadership in love, career, finances, and twin flame connections.",
    "crystal": "Opalite",
    "frequency": "Rare",
    "color": "#d4bfe8",
    "intro": "When the new beginnings of 1 intersect with the massive changes of 5, the sequence 1155 signals a period of significant transformation that requires the individual to assume a strong leadership role. It demands courage to lean into intuition and navigate incoming shifts that may initially seem chaotic. This sequence warns that passivity is no longer an option; the individual must take the helm and actively steer their life through the transition.",
    "why": "The consistent observation of 1155 is a dramatic sign that your life is about to undergo significant, paradigm-altering transformations. It demands that you embrace these changes by stepping into a strong leadership role and trusting your inner intuition completely. Your angels are confirming that making bold changes now will lead to highly positive outcomes.",
    "general": "The sequence 1155 is a dramatic sign that your life is about to undergo significant, paradigm-altering transformations. It demands that you embrace these changes by stepping into a strong leadership role and trusting your inner intuition completely. Your angels are confirming that making bold changes now will lead to highly positive outcomes.",
    "love": "Your love life is experiencing a profound rejuvenation, bringing a wave of optimism and potential new beginnings. You must take the initiative to introduce fresh energy into your relationships or actively seek out new romantic connections. It is a critical period for couples to break routines and redefine the parameters of their connection.",
    "career": "You are stepping into exciting new leadership roles or overseeing innovative projects that completely alter your professional trajectory. Embrace these career changes with open arms, as they are vitally necessary for your ultimate vocational growth. The sequence encourages the individual to lean into massive shifts rather than resisting them.",
    "finance": "Financial progress requires you to take calculated risks and initiate new wealth-building endeavors without hesitation. Trust that the changes you implement now will drastically improve your material stability over time. The sequence warns strongly against financial rigidity during this highly dynamic transit.",
    "twin_flame": "The twin flame dynamic is undergoing rapid, essential shifts that require both partners to adapt quickly and fearlessly. Embrace this period of transformation, as it is designed to clear old blockages and elevate the soul connection. The sequence forces both individuals completely out of their comfort zones.",
    "action": "Greet impending life changes with open arms, step into a leadership mindset, and execute new projects without fear."
  },
  1212: {
    "title": "Spiritual Ascension and Destined Alignment",
    "h1": "Decoding Angel Number 1212: The Rhythmic Dance of Action and Trust",
    "meta": "Delve into the harmonious energy of angel number 1212. Understand its profound impact on spiritual balance, career abundance, deep love, and twin flames.",
    "crystal": "Clear Quartz",
    "frequency": "Common",
    "color": "#c9a96e",
    "intro": "The sequence 1212 possesses a structural uniqueness within the angel number system, serving as an alternating rhythm rather than a simple repetition of a single digit. This pattern weaves together the pioneering, independent, and action-oriented energy of the number 1 with the cooperative, receptive, and harmonious wisdom of the number 2. Furthermore, through numerological reduction, the sequence ultimately anchors into the vibration of the number 6, representing domestic stability, family, and deep responsibility.",
    "why": "The consistent observation of 1212 indicates that the individual is in a phase of profound spiritual completeness and is being called to step forward courageously while simultaneously allowing the universe to handle the intricate details. It appears when the observer must learn that taking initiative and practicing surrender are not mutually exclusive, but rather complementary steps in the delicate dance of manifestation. The universe presents 1212 to confirm that the individual's energetic output is perfectly aligned with their highest purpose.",
    "general": "The sequence 1212 is a powerful confirmation that you are perfectly in line with your ultimate destiny and experiencing spiritual ascension. It blends the independent drive of new beginnings with the harmonious patience of deep emotional healing. Your guardian angels are actively supporting your progress toward a higher state of being.",
    "love": "Positive changes are transforming your love life, bringing a perfect balance of independence and deeply supportive partnership. It indicates that your current romantic trajectory is destined and highly favored by the universe. For single individuals, 1212 is a powerful omen that love is on the immediate horizon.",
    "career": "You are successfully navigating professional shifts by taking confident initiative while maintaining excellent cooperative relationships with peers. Your career is advancing steadily because your actions are aligned with your true purpose. The sequence represents the sweet spot where independent ambition aligns perfectly with cooperative teamwork.",
    "finance": "Financial stability is being achieved through a balanced approach to generating new income and managing existing resources responsibly. Trust that your financial destiny is secure as long as you maintain a positive, progressive mindset. Your mental energy is actively drawing monetary blessings and unexpected opportunities into your reality.",
    "twin_flame": "This is a powerful twin flame number symbolizing a new depth of harmony, unity, and the manifestation of a shared life. It confirms that you and your twin flame are in perfect alignment and the connection is rapidly strengthening. The sequence acts as a definitive sign that the twin flame is drawing closer.",
    "action": "Maintain an optimistic outlook, confidently step out of your comfort zone, and trust the divine guidance leading your path."
  },
  1234: {
    "title": "Progressive Momentum and Evolution",
    "h1": "The Power of Progression: Manifesting with Angel Number 1234",
    "meta": "Discover the momentum of angel number 1234. Learn how this sequential pattern drives step-by-step progress in love, career, wealth, and twin flame unions.",
    "crystal": "Citrine",
    "frequency": "Common",
    "color": "#c9a96e",
    "intro": "The numeric sequence 1234 stands completely apart from repeating digits by illustrating a clear, sequential progression, radiating an energy of relentless forward momentum and systematic evolution. This progressive sequence outlines a specific metaphysical architecture where an initial idea is fiercely initiated (digit 1), subsequently balanced through deep intuition and partnership (digit 2), aggressively expanded through vibrant creative action (digit 3), and finally grounded into a stable, lasting foundation (digit 4).",
    "why": "When an individual continuously observes 1234, the universe is confirming that they are unequivocally on the right path and actively moving toward their highest potential. This sequence frequently appears to encourage the individual to massively simplify their life, eliminate superficial distractions, and adopt a highly disciplined, step-by-step approach to their objectives. It is a powerful reminder that massive life changes cannot be achieved overnight; they require deep personal development and the willingness to sequentially lay down the necessary groundwork.",
    "general": "The ascending sequence 1234 indicates that you are gaining unstoppable momentum and moving systematically through the necessary stages of personal evolution. It is a highly progressive vibration that confirms your step-by-step efforts are leading to significant success. You are leveling up and building an unshakeable foundation for your future.",
    "love": "Your relationship is naturally progressing to the next level of commitment through consistent effort and mutual support. For singles, it advises taking proactive, logical steps to seek out a partner rather than waiting passively. Love is an active progression, not a passive state, requiring constant forward motion.",
    "career": "Your hard work is compounding, and you are currently preparing for a major professional payoff or leveling up in your industry. It is an excellent time to systematically plan and launch a new business venture or project. By maintaining dedication and trusting your decision-making capabilities, you will systematically ascend the professional ladder.",
    "finance": "Consistent, incremental financial strategies are steadily building a highly secure and expansive wealth portfolio. Focus on higher-level financial thinking and practical investments rather than seeking immediate, unstructured gains. Master fundamental financial principles and sequentially execute an innovative strategy for long-term prosperity.",
    "twin_flame": "The twin flame connection is steadily ascending through its destined stages of evolution and shadow work. If experiencing drama or separation, trust that this is merely a temporary step on the definitive path toward ultimate reunion. The sequence highlights the necessity of healing the trinity of core upsets common to twin flames: wealth, intimacy, and communication.",
    "action": "Continue putting in consistent, hard work and take the next logical step forward without skipping vital parts of the process."
  },
  2222: {
    "title": "Profound Harmony and Dual Mastery",
    "h1": "Angel Number 2222: Mastering Duality and Achieving Perfect Harmony",
    "meta": "Explore angel number 2222 meaning. Discover how this master sequence guides emotional balance, love alignment, career stability, and twin flame reunions.",
    "crystal": "Rose Quartz & Blue Sapphire",
    "frequency": "Rare",
    "color": "#b8d4e8",
    "intro": "Amplifying the harmonizing energy of 2 to its maximum extent, the sequence 2222 is a double master number that serves as the ultimate beacon of peace, emotional stability, and profound relational alignment. It offers deep comfort during periods of severe doubt, confirming that emotional stability leads to lasting success. The mathematical reduction of 2+2+2+2 equals 8, bridging the concept of emotional harmony with the number 8's promise of long-term material success.",
    "why": "The powerful sequence 2222 represents the ultimate mastery of balance, duality, and profound emotional harmony. It serves as a strong reassurance from the spiritual realm that you are perfectly aligned with your higher self and the universe. Even if progress seems incredibly slow, you are urged to maintain unshakeable patience and inner peace.",
    "general": "The powerful sequence 2222 represents the ultimate mastery of balance, duality, and profound emotional harmony. It serves as a strong reassurance from the spiritual realm that you are perfectly aligned with your higher self and the universe. Even if progress seems incredibly slow, you are urged to maintain unshakeable patience and inner peace.",
    "love": "This is the ultimate number of romantic alignment, indicating that deep emotional harmony and mutual respect are anchoring your relationship. If single, love will develop naturally and effortlessly once you completely restore your own internal emotional balance. The sequence offers immense comfort during periods of agonizing separation or misunderstanding.",
    "career": "You are steadily progressing in the right direction, and your dedicated, positive energy is quietly guiding you toward major success. It emphasizes the absolute necessity of maintaining a healthy work-life balance to avoid burnout. Optimal professional success will be achieved not in isolation, but by harnessing personal initiative to lead collaborative efforts.",
    "finance": "Your financial situation is achieving remarkable stability and long-term security through a highly balanced, patient approach to wealth. Avoid any impulsive economic choices and trust that steady, gradual progress will yield massive financial rewards. Take a cooperative approach to wealth management, possibly seeking wise counsel of fiduciary advisors.",
    "twin_flame": "Considered a primary twin flame beacon, 2222 indicates that a destined reunion is imminent as both souls achieve energetic equilibrium. It demands profound patience, requiring both individuals to heal individually before merging into a perfectly harmonious union. The sequence signifies that beneath the surface turbulence, the foundational energies of the two souls are actively working toward alignment.",
    "action": "Pause before reacting to any situation, prioritize your emotional calm, and trust that perfect alignment is happening behind the scenes."
  },
  3333: {
    "title": "Expressive Synergy and Boundless Optimism",
    "h1": "Angel Number 3333: Unleashing Creative Synergy and Boundless Optimism",
    "meta": "Discover the meaning of angel number 3333. Learn how this powerful sequence activates creativity, deepens love, supercharges career, and advances twin flames.",
    "crystal": "Carnelian",
    "frequency": "Rare",
    "color": "#e8d070",
    "intro": "The quadruplication of 3 in the sequence 3333 results in a massive surge of optimism, social connectivity, and highly expressive energy. It is a divine push to abandon isolation, communicate openly, and utilize one's talents to inspire the collective. The energetic vibration of 3333 can be compared to the perfect, optimistic balance between the energy received from the sun and the energy radiated back out into space — absorbing divine inspiration and actively radiating it outward through creative and social pursuits.",
    "why": "The sequence 3333 is an explosive manifestation of creative energy, social connection, and boundless optimism. It indicates that your innate talents have been fully activated by the divine, urging you to express yourself with absolute joy. You are being called to break out of your routine, become highly adventurous, and inspire those around you.",
    "general": "The sequence 3333 is an explosive manifestation of creative energy, social connection, and boundless optimism. It indicates that your innate talents have been fully activated by the divine, urging you to express yourself with absolute joy. You are being called to break out of your routine, become highly adventurous, and inspire those around you.",
    "love": "Honest, highly expressive communication will drastically deepen the bond you share with your partner. For singles, this vibrant energy acts as a magnet, signaling that your true love is right around the corner if you socialize actively. The sequence demands the complete dismantling of communication barriers and the cessation of secretive behavior.",
    "career": "Extensive networking and collaborative teamwork are the immediate keys to unlocking massive advancement in your career. You must boldly share your innovative ideas and utilize your unique creative skills to distinguish yourself professionally. The sequence is highly favorable for individuals operating in creative, communicative, or media-driven industries.",
    "finance": "Financial abundance is highly favored, often manifesting through lucrative investments, creative ventures, or collaborative business partnerships. However, the sequence warns against greed, urging you to align your spending perfectly with your life's higher purpose. Financial growth is inextricably linked to the ability to seamlessly collaborate with others.",
    "twin_flame": "You are on the precipice of an imminent and highly communicative encounter or reunion with your twin flame. While the journey may involve challenging separations to inspire growth, your ultimate reunion will be built on unbreakable harmony. It encourages both twins to focus intensely on their individual creative missions.",
    "action": "Socialize aggressively, communicate your deepest feelings openly, and boldly pursue your most creative impulses."
  },
  4444: {
    "title": "Impenetrable Stability and Divine Affirmation",
    "h1": "Angel Number 4444: Building an Impenetrable Fortress of Stability",
    "meta": "Understand angel number 4444 meaning. Discover how this sequence confirms divine protection, accelerates career building, stabilizes love, and guides twin flames.",
    "crystal": "Black Tourmaline",
    "frequency": "Rare",
    "color": "#8899aa",
    "intro": "The sequence 4444 amplifies the foundational energy of 4 to its maximum limit, creating a metaphorical fortress of stability and divine protection. It signifies a dramatic shift in fortune brought about by relentless determination, extreme organization, and the overcoming of significant obstacles. When an individual encounters 4444, they are being assured that the architecture of their life — built through grueling, disciplined effort — is finally solidifying.",
    "why": "The sequence 4444 represents impenetrable stability, relentless determination, and absolute affirmation from the divine realm. It is a powerful signal of progress, indicating that you have the spiritual support to overcome any current challenges. Your guardian angels are confirming that your highly disciplined approach is shifting your fortune positively.",
    "general": "The sequence 4444 represents impenetrable stability, relentless determination, and absolute affirmation from the divine realm. It is a powerful signal of progress, indicating that you have the spiritual support to overcome any current challenges. Your guardian angels are confirming that your highly disciplined approach is shifting your fortune positively.",
    "love": "Your romantic life is experiencing highly positive developments that will lead to a remarkably secure and structured partnership. It provides deep reassurance that your current relationship is built to withstand any external pressures or difficulties. The sequence indicates a time of great harmony where massive investments in understanding and supporting one another are bearing fruit.",
    "career": "Your relentless hard work and unyielding dedication are about to be rewarded with significant, tangible career advancements. You have established a flawless professional foundation that will easily support long-term success and heavy responsibilities. Lasting success will be achieved strictly through relentless consistency, discipline, and a focus on long-term structural integrity.",
    "finance": "You are entering a period of immense financial success and absolute economic protection against material hardship. Continue your disciplined wealth management, as your systematic efforts are guaranteeing a highly prosperous future. The sequence emphasizes conservative, methodical wealth accumulation over speculative or high-risk ventures.",
    "twin_flame": "The twin flame dynamic is experiencing crucial growth, moving from a phase of turbulence into a deeply grounded, stable connection. It offers profound reassurance that the structural integrity of your soul bond is entirely protected by the universe. The sequence encourages both individuals to do the practical, unglamorous psychological work required.",
    "action": "Keep moving forward with relentless determination, trusting that your foundations are secure and divine guidance is ever-present."
  },
  5555: {
    "title": "Absolute Metamorphosis and Liberation",
    "h1": "Angel Number 5555: The Catalyst of Absolute Metamorphosis",
    "meta": "Explore the transformative meaning of angel number 5555. Learn how this sequence catalyzes radical life changes in love, career, finances, and twin flames.",
    "crystal": "Labradorite",
    "frequency": "Rare",
    "color": "#70c8b0",
    "intro": "When the dynamic energy of 5 is quadrupled into 5555, the resulting frequency represents absolute, systemic life metamorphosis. It demands extreme adaptability and the courage to take monumental risks, ensuring the individual breaks completely free from stagnant paradigms. Unlike the gentle progression of other numbers, 5555 operates as a wrecking ball to complacency, notifying the individual that holding onto the past is futile.",
    "why": "The extremely potent sequence 5555 acts as a catalyst for absolute metamorphosis and complete liberation from stagnant life paradigms. It signifies that unprecedented, monumental shifts are arriving to overhaul your entire existence. You must possess the courage to break old patterns completely and trust in your ability to navigate massive transitions.",
    "general": "The extremely potent sequence 5555 acts as a catalyst for absolute metamorphosis and complete liberation from stagnant life paradigms. It signifies that unprecedented, monumental shifts are arriving to overhaul your entire existence. You must possess the courage to break old patterns completely and trust in your ability to navigate massive transitions.",
    "love": "You must completely abandon outdated relationship patterns to foster genuine connections and remain radically open to new romantic opportunities. Existing relationships will undergo a massive transformation that redefines the fundamental nature of the partnership. A sudden, highly unexpected encounter may entirely alter your romantic landscape.",
    "career": "Positive, radical shifts in your career are imminent, requiring you to take bold risks and pursue highly ambitious projects. Trust entirely in your professional abilities, as these sudden disruptions will lead directly to greater prosperity and freedom. By remaining highly adaptable and trusting your innate abilities, you will discover roles that offer greater autonomy.",
    "finance": "Embracing adaptability and taking calculated financial risks during this period of upheaval will lead to massive economic rewards. You must manage your resources wisely as entirely new, unexpected avenues for generating wealth rapidly unfold. The sequence warns strongly against financial rigidity and clinging to outdated investment strategies.",
    "twin_flame": "The twin flame connection is undergoing an extreme, necessary transformation to facilitate profound healing and spiritual progress. If separated, this intense period of change is actively destroying old karmic blocks to prepare both souls for a redefined reunion. The twins must rapidly adapt to higher frequencies of unconditional love.",
    "action": "Believe absolutely in your abilities, embrace monumental risks, and allow the universe to completely transform your reality."
  },
  6666: {
    "title": "Profound Healing and Shadow Work",
    "h1": "Angel Number 6666: The Call for Deep Healing and Spiritual Restructuring",
    "meta": "Discover the meaning of angel number 6666. Learn how this sequence calls for profound self-healing, relational balance, career alignment, and twin flame work.",
    "crystal": "Rhodochrosite",
    "frequency": "Rare",
    "color": "#f0a0b8",
    "intro": "Amplifying the healing frequency of 6, the sequence 6666 is an intense, localized intervention for psychological and spiritual recovery. It demands the subject confront their deepest shadows, rectify internal imbalances, and engage in radical self-acceptance. Astrologically linked to Pisces, this sequence encourages diving into the realms of the subconscious and dreaming. Furthermore, it corresponds with The Lovers card in Tarot, highlighting deep soul mate love and the necessity of healing past relationship traumas.",
    "why": "The sequence 6666 is a highly spiritual message calling for profound internal healing and the establishment of absolute harmony within yourself. It prompts you to dive deeply into your subconscious, release past wounds, and completely embrace unconditional self-love. You are being guided to correct severe imbalances between your material desires and spiritual needs.",
    "general": "The sequence 6666 is a highly spiritual message calling for profound internal healing and the establishment of absolute harmony within yourself. It prompts you to dive deeply into your subconscious, release past wounds, and completely embrace unconditional self-love. You are being guided to correct severe imbalances between your material desires and spiritual needs.",
    "love": "You must establish a healthy sense of boundaries and engage in emotional restructuring within your romantic relationships. True partnership requires you to deeply understand your own emotional architecture and love yourself without any judgment or condition. True relational harmony can only be achieved when you first offer unconditional love and acceptance to yourself.",
    "career": "It is critical to let go of negative thoughts and severe anxieties regarding your professional trajectory to allow for positive developments. You must ruthlessly enforce a healthy work-life balance, ensuring that ambition does not destroy your personal well-being. It is an optimal time to establish strict boundaries and find intrinsic joy in daily tasks.",
    "finance": "This number emphasizes the absolute necessity of aligning your material financial goals strictly with your higher spiritual values. True financial success and abundance will only be fulfilling when achieved through ethical, meaningful work and balanced resource management. Release gripping fears regarding material needs, trusting that a balanced approach will naturally attract abundance.",
    "twin_flame": "This is a critical twin flame sequence offering a message of intense hope and deep psychological healing during periods of separation. It demands that both individuals focus entirely on personal shadow work, releasing past traumas to prepare for a stable union. The observer must redirect immense energy inward to heal themselves first.",
    "action": "Engage aggressively in deep self-exploration, release all self-judgment, and restructure your life to prioritize holistic balance."
  },
  7777: {
    "title": "Ultimate Cosmic Alignment and Reward",
    "h1": "Angel Number 7777: The Pinnacle of Universal Alignment and Cosmic Reward",
    "meta": "Uncover the rare meaning of angel number 7777. Discover how this sequence signals the pinnacle of spiritual growth, love fulfillment, career success, and twin flames.",
    "crystal": "Amethyst",
    "frequency": "Rare",
    "color": "#9b6bbf",
    "intro": "The extremely rare sequence 7777 represents the highest echelon of spiritual growth, esoteric intuition, and cosmic reward. It signifies that the individual's dedication to their spiritual practices, ethical behavior, and vocational paths has resulted in profound alignment with the universe, triggering an influx of success. To see this number is to be told by the cosmos that one is operating at peak intuitive capacity.",
    "why": "The extraordinarily rare sequence 7777 signifies the absolute pinnacle of spiritual growth, esoteric wisdom, and perfect cosmic alignment. It is a powerful confirmation that your intense dedication to your personal evolution is being actively rewarded by the higher realms. You are encouraged to trust your highly attuned intuition, as it is leading you flawlessly.",
    "general": "The extraordinarily rare sequence 7777 signifies the absolute pinnacle of spiritual growth, esoteric wisdom, and perfect cosmic alignment. It is a powerful confirmation that your intense dedication to your personal evolution is being actively rewarded by the higher realms. You are encouraged to trust your highly attuned intuition, as it is leading you flawlessly.",
    "love": "Your romantic connections are heavily influenced by deep spiritual dynamics, requiring a profound, soulful resonance with your partner. It indicates that your relational life is evolving rapidly toward a state of enlightened, unconditional mutual support. The connection possesses genuine, profound spiritual depth that bypasses standard psychological overthinking.",
    "career": "You are currently welcoming massive professional success because your career choices are perfectly aligned with your soul's true purpose. Your relentless dedication and persistence are being universally recognized, opening doors to highly prestigious new opportunities. The sequence provides the strongest possible confirmation that the current career path is correct and highly favored.",
    "finance": "Immense financial rewards are manifesting rapidly as a direct consequence of your spiritual integrity and hard work. However, the universe strongly encourages you to utilize this sudden wealth to enhance your holistic quality of life. The sequence indicates that the observer is closer to financial stability than they realize.",
    "twin_flame": "This is a phenomenally powerful sign indicating complete spiritual healing, imminent reunion, and explosive personal growth within the twin flame journey. Both souls have successfully navigated profound self-discovery and are now prepared for an incredibly deep, harmonious connection. The sequence signals that both individuals have evolved to a similar frequency.",
    "action": "Trust your heightened intuition implicitly and gratefully accept the massive success flowing into your reality."
  },
  8888: {
    "title": "Infinite Prosperity and Material Mastery",
    "h1": "Angel Number 8888: Entering the Vortex of Infinite Prosperity",
    "meta": "Discover the meaning of angel number 8888. Learn how this sequence signals infinite prosperity, career mastery, relationship abundance, and twin flame fulfillment.",
    "crystal": "Citrine",
    "frequency": "Rare",
    "color": "#c9a96e",
    "intro": "Expanding the financial and karmic mastery of 8 into a quadruplicate, 8888 creates a literal energetic vortex of infinite prosperity and immense karmic payouts. It represents the total mastery of the material realm achieved exclusively through rigorous spiritual alignment, ensuring a continuous windfall of blessings. When 8888 appears, the individual is stepping out of linear time regarding wealth generation and entering an infinite loop of receiving and giving.",
    "why": "The sequence 8888 represents the opening of a massive energetic vortex delivering infinite prosperity, profound blessings, and ultimate karmic payouts. It signifies that your spiritual alignment has resulted in total mastery over the material realm. You are advised to stay highly connected and spiritually open to receive the monumental windfalls coming your way.",
    "general": "The sequence 8888 represents the opening of a massive energetic vortex delivering infinite prosperity, profound blessings, and ultimate karmic payouts. It signifies that your spiritual alignment has resulted in total mastery over the material realm. You are advised to stay highly connected and spiritually open to receive the monumental windfalls coming your way.",
    "love": "Your romantic life is overflowing with abundant, deeply fulfilling energy that reflects the immense love you have cultivated within. It signifies a partnership that acts as a powerhouse for mutual success, joy, and boundless emotional wealth. Your love life is entering a phase of rich emotional abundance and deeply reciprocal exchange.",
    "career": "You are achieving unprecedented, monumental success in your career, commanding absolute authority and respect within your industry. This is a time of massive expansion, where your professional influence and capabilities are recognized as limitless. The sequence signifies major professional advancement and the attainment of high-level leadership positions.",
    "finance": "An extraordinary, life-altering financial windfall is arriving, cementing your absolute economic security and wealth generation. You are currently experiencing the ultimate peak of financial flow, driven by your past ethical actions and high vibrational state. Wealth must be managed with high integrity and utilized to create positive impacts within the broader ecosystem.",
    "twin_flame": "The twin flame union is functioning as an infinite feedback loop of highly positive, expansive energy that empowers both individuals. Together, you are manifesting immense earthly success and fulfilling a deeply significant, shared cosmic mission. The intense karmic debts often associated with twin flame dynamics have been largely balanced.",
    "action": "Remain completely spiritually open, graciously accept the monumental financial windfalls, and utilize your abundance to elevate others."
  },
  9999: {
    "title": "Ultimate Completion and Total Soul Renewal",
    "h1": "Angel Number 9999: The Ultimate Paradigm Conclusion and Total Soul Renewal",
    "meta": "Understand the profound meaning of angel number 9999. Discover what this sequence signals for life completion, love transitions, career shifts, and twin flames.",
    "crystal": "Selenite",
    "frequency": "Rare",
    "color": "#c84848",
    "intro": "The sequence 9999 serves as the absolute terminus of the numerological spectrum. It denotes the finality of massive life chapters, profound soul renewal, and the complete shedding of past karmic identities to prepare for a totally unprecedented existence. It requires the individual to perform a total systemic purge — emotionally, materially, and spiritually. Resisting the endings heralded by 9999 creates immense friction, whereas surrendering clears the metaphysical slate entirely.",
    "why": "The sequence 9999 is the most definitive signal of ultimate completion, massive life transitions, and profound soul renewal. It indicates that a monumental, long-standing karmic chapter of your existence has reached its absolute conclusion. You are being completely cleared of past identities to prepare for entry into a totally unprecedented, higher paradigm.",
    "general": "The sequence 9999 is the most definitive signal of ultimate completion, massive life transitions, and profound soul renewal. It indicates that a monumental, long-standing karmic chapter of your existence has reached its absolute conclusion. You are being completely cleared of past identities to prepare for entry into a totally unprecedented, higher paradigm.",
    "love": "A major cycle within your romantic life has finished, requiring the absolute release of any relationships or toxic dynamics that hinder your growth. You must engage in deep forgiveness and let go of all emotional baggage to welcome an evolved state of love. For those in partnerships, 9999 may indicate the end of one phase and the rapid beginning of a deeper commitment.",
    "career": "Your current professional identity has been entirely outgrown, signaling an imminent, total transition toward your ultimate life vocation. You are urged to fearlessly abandon unfulfilling career paths to embrace a completely new, spiritually aligned mission. The sequence heralds a period of significant, often total professional transition.",
    "finance": "Old financial structures, limiting economic beliefs, and previous methods of generating wealth are being permanently dismantled. This profound clearing paves the way for a completely refreshed, highly ethical approach to universal abundance. It is time to definitively end poor financial practices and aggressively pay off lingering debts.",
    "twin_flame": "The twin flame connection has successfully completed a massive, grueling karmic cycle of separation, learning, and deep healing. This ultimate closure is the final, necessary step before both souls can fully ascend into a permanent, harmonious union. The sequence frequently serves as the universe's mechanism for revealing a false twin flame.",
    "action": "Surrender completely to these massive endings, release all fear of the unknown, and prepare your soul for total renewal."
  }
}

FREQ_COLOR = {"Very Common": "#1D9E75", "Common": "#c9a96e", "Rare": "#c84848"}

# ─── HTML Template ───────────────────────────────────────
def make_page(n, d):
    fc = FREQ_COLOR.get(d["frequency"], "#9b6bbf")
    
    # Related numbers
    all_nums = sorted(DATA.keys())
    others = [x for x in all_nums if x != n]
    related_html = "\n".join([
        f'<a href="/angel-number-{x}/" style="display:inline-block;background:rgba(255,255,255,.6);border:1px solid rgba(155,107,191,.2);border-radius:10px;padding:7px 12px;text-align:center;text-decoration:none;margin:4px;"><span style="font-family:Playfair Display,serif;font-size:16px;font-weight:700;color:{DATA[x]["color"]};display:block;">{x}</span><span style="font-size:9.5px;color:#a08878;">{DATA[x]["title"].split(" ")[0]}</span></a>'
        for x in others[:12]
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Angel Number {n} Meaning — {d["title"]} | Lumina Numbers</title>
<meta name="description" content="{d["meta"]}">
<meta property="og:title" content="Angel Number {n} — {d["title"]} | Lumina Numbers">
<meta property="og:description" content="{d["meta"]}">
<meta property="og:image" content="/og-image.jpg">
<link rel="canonical" href="https://luminanumbers.com/angel-number-{n}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="/js/cookie-consent.js" data-ga="{GA_ID}"></script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--cream:#fdf8f2;--gold:#c9a96e;--lav:#9b6bbf;--text-dark:#2d2418;--text-mid:#6b5744;--text-soft:#a08878;--glass:rgba(255,255,255,0.6);--glass-border:rgba(201,169,110,0.22);--shadow:0 8px 32px rgba(180,140,100,0.13)}}
body{{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--text-dark);overflow-x:hidden;-webkit-font-smoothing:antialiased}}
.bg{{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse 80% 60% at 70% 10%,rgba(212,191,232,.4) 0%,transparent 60%),radial-gradient(ellipse 55% 50% at 15% 80%,rgba(232,213,176,.32) 0%,transparent 55%),var(--cream)}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 5vw;height:64px;background:rgba(253,248,242,.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(201,169,110,.13)}}
.nl{{display:flex;align-items:center;gap:9px;text-decoration:none}}
.ni{{width:32px;height:32px;background:linear-gradient(135deg,#e8d5b0,#c9a96e);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px}}
.nn{{font-family:'Playfair Display',serif;font-size:15px;font-weight:600;color:var(--text-dark);letter-spacing:.07em}}
.ns{{font-size:9px;letter-spacing:.1em;color:var(--gold);text-transform:uppercase}}
.nb{{font-size:13px;color:var(--text-soft);text-decoration:none;transition:color .2s}}
.nb:hover{{color:var(--gold)}}
.hero{{position:relative;z-index:1;padding:88px 5vw 40px;text-align:center;max-width:800px;margin:0 auto}}
.ey{{font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--lav);margin-bottom:12px;display:flex;align-items:center;justify-content:center;gap:8px}}
.ey::before,.ey::after{{content:'✦';font-size:9px}}
.big-num{{font-family:'Playfair Display',serif;font-size:clamp(72px,18vw,110px);font-weight:700;line-height:1;color:{d["color"]};margin-bottom:8px}}
h1{{font-family:'Playfair Display',serif;font-size:clamp(22px,4vw,38px);line-height:1.15;color:var(--text-dark);margin-bottom:10px}}
.freq-pill{{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.6);border:1px solid rgba(155,107,191,.22);border-radius:99px;padding:5px 14px;font-size:12px;color:var(--lav);font-weight:500;margin-bottom:8px}}
.crystal-pill{{display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,.55);border:1px solid rgba(201,169,110,.2);border-radius:99px;padding:5px 12px;font-size:11.5px;color:var(--text-mid);margin-left:6px}}
.content{{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:28px 5vw 80px}}
.card{{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow)}}
.ct{{font-family:'Playfair Display',serif;font-size:16px;font-weight:600;color:var(--text-dark);margin-bottom:12px;display:flex;align-items:center;gap:7px}}
.ct::before{{content:attr(data-icon);font-size:17px}}
.ctext{{font-size:14px;color:var(--text-mid);line-height:1.8}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
.action-card{{background:linear-gradient(135deg,rgba(155,107,191,.15),rgba(212,191,232,.15));border:1px solid rgba(155,107,191,.25);border-radius:16px;padding:16px 18px;margin-bottom:16px;display:flex;align-items:flex-start;gap:12px}}
.action-icon{{font-size:22px;flex-shrink:0;margin-top:2px}}
.action-label{{font-size:11px;font-weight:500;letter-spacing:.07em;text-transform:uppercase;color:var(--lav);margin-bottom:4px}}
.forecast-c{{background:linear-gradient(135deg,rgba(201,169,110,.15),rgba(245,196,168,.15));border:1px solid rgba(201,169,110,.25);border-radius:20px;padding:22px;margin-bottom:16px}}
.cta-c{{background:linear-gradient(135deg,rgba(212,191,232,.3),rgba(155,107,191,.15));border:1px solid rgba(155,107,191,.2);border-radius:20px;padding:24px;margin-bottom:16px;text-align:center}}
.btn-cta{{display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,#c4a0e0,#9b6bbf);color:white;border:none;border-radius:14px;padding:13px 24px;font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;cursor:pointer;text-decoration:none;box-shadow:0 6px 18px rgba(155,107,191,.35);transition:transform .15s}}
.btn-cta:hover{{transform:translateY(-1px)}}
@media(max-width:600px){{.two{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="bg"></div>
<nav>
  <a href="/" class="nl">
    <div class="ni">✦</div>
    <div>
      <div class="nn">LUMINA NUMBERS</div>
      <div class="ns">Discover Your Divine Numbers</div>
    </div>
  </a>
  <a href="/angel-numbers/" class="nb">← All Angel Numbers</a>
</nav>

<div class="hero">
  <div class="ey">Angel Number {n}</div>
  <div class="big-num">{n}</div>
  <h1>{d["h1"].replace(f"Angel Number {n}: ", "").replace(f"Angel Number {n} — ", "")}</h1>
  <div style="margin-top:10px">
    <span class="freq-pill" style="color:{fc}"><span style="color:{fc}">●</span> {d["frequency"]}</span>
    <span class="crystal-pill">💎 {d["crystal"]}</span>
  </div>
</div>

<div class="content">

  <div class="card">
    <div class="ct" data-icon="📖">Overview</div>
    <p class="ctext">{d["intro"]}</p>
  </div>

  <div class="card" style="background:linear-gradient(135deg,rgba(155,107,191,.1),rgba(212,191,232,.1));border-color:rgba(155,107,191,.22);">
    <div class="ct" data-icon="🔍">Why Am I Seeing {n}?</div>
    <p class="ctext">{d["why"]}</p>
  </div>

  <div class="action-card">
    <div class="action-icon">⚡</div>
    <div>
      <div class="action-label">Your Action Right Now</div>
      <p class="ctext">{d["action"]}</p>
    </div>
  </div>

  <div class="two">
    <div class="card" style="background:linear-gradient(135deg,rgba(232,164,176,.18),rgba(212,191,232,.18));border-color:rgba(232,164,176,.28);">
      <div class="ct" data-icon="♡">Love & Relationships</div>
      <p class="ctext">{d["love"]}</p>
    </div>
    <div class="card">
      <div class="ct" data-icon="💼">Career & Purpose</div>
      <p class="ctext">{d["career"]}</p>
    </div>
  </div>

  <div class="two">
    <div class="card">
      <div class="ct" data-icon="💰">Finance & Abundance</div>
      <p class="ctext">{d["finance"]}</p>
    </div>
    <div class="card" style="background:linear-gradient(135deg,rgba(245,196,168,.2),rgba(232,164,176,.15));border-color:rgba(232,164,176,.25);">
      <div class="ct" data-icon="🔥">Twin Flame</div>
      <p class="ctext">{d["twin_flame"]}</p>
    </div>
  </div>

  <div class="forecast-c">
    <div style="font-size:11px;font-weight:500;letter-spacing:.07em;text-transform:uppercase;color:var(--gold);margin-bottom:8px">✦ General Message</div>
    <p class="ctext">{d["general"]}</p>
  </div>

  <div class="cta-c">
    <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:600;color:var(--text-dark);margin-bottom:8px">Decode Your Angel Number Live</div>
    <p style="font-size:13.5px;color:var(--text-soft);margin-bottom:18px">Enter your number and add the exact date you saw it for a personalised combined reading.</p>
    <a href="/angel-numbers/" class="btn-cta">🪽 Open Angel Number Decoder →</a>
  </div>

  <div class="card">
    <div class="ct" data-icon="🪽">Explore More Angel Numbers</div>
    <div style="margin-top:6px">{related_html}</div>
  </div>

</div>
</body>
</html>"""

# ─── Generate ────────────────────────────────────────────
def make_dir(path):
    os.makedirs(path, exist_ok=True)

def write(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

count = 0
print("Generating angel number pSEO pages...")
for n, d in DATA.items():
    folder = os.path.join(BASE, f"angel-number-{n}")
    make_dir(folder)
    write(os.path.join(folder, "index.html"), make_page(n, d))
    print(f"  🪽 /angel-number-{n}/")
    count += 1

# ─── Update sitemap ──────────────────────────────────────
print("\nUpdating sitemap.xml...")
sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    existing = f.read()

# Build new angel number URLs
angel_urls = ""
for n in sorted(DATA.keys()):
    angel_urls += f"""  <url>
    <loc>https://luminanumbers.com/angel-number-{n}/</loc>
    <lastmod>2026-05-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

# Also add angel-numbers tool page if not present
tool_url = """  <url>
    <loc>https://luminanumbers.com/angel-numbers/</loc>
    <lastmod>2026-05-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>\n"""

# Insert before closing tag
new_sitemap = existing.replace("</urlset>", tool_url + angel_urls + "</urlset>")
write(sitemap_path, new_sitemap)
print("  ✦ sitemap.xml updated")

print(f"\n✦ Done! Generated {count} angel number pages")
print(f"  - {count} pSEO pages: /angel-number-111/ to /angel-number-9999/")
print(f"  - sitemap.xml updated with all URLs")
print(f"\nNext: GitHub Desktop → Commit 'add angel number pSEO pages' → Push → Done!")
