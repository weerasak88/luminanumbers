"""
Lumina Numbers — pSEO Generator
สร้าง: /life-path-[n]-meaning/ (12 หน้า)
       /life-path-[n1]-and-[n2]-compatibility/ (66 หน้า)
รัน: python generate_pseo.py
"""

import os

BASE = r"C:\zkambheer\luminanumbers"

# ─── Data ───────────────────────────────────────────────
DATA = {
  1:{"title":"The Pioneer","planet":"Sun","color":"Gold, Orange, Red","colorHex":"#c9a96e","day":"Sunday",
    "overview":"Governed by the radiant energy of the Sun, Life Path 1 individuals are natural-born leaders destined to forge unprecedented trails and initiate progress. They must learn to balance fierce independence with collaboration, acting as the spark that illuminates the path for others without burning them.",
    "meta_desc":"Discover Life Path 1 meaning — The Pioneer. Core traits, strengths, ideal careers, love compatibility, and your 2026 numerology forecast.",
    "strengths":["Visionary and authoritative leadership","Unwavering self-reliance","Courageous entrepreneurial initiative","Creative and rapid problem-solving","Exceptional resilience against adversity"],
    "challenges":["Unchecked egotism and stubbornness","Impatience with those who process slowly","Tendency to dominate relationships"],
    "love":"Fiercely passionate and highly protective, they seek a robust partner who respects their absolute need for autonomy while matching their intense energy. They naturally assume the dominant role and require a deeply passionate, non-restrictive bond.",
    "careers":["Entrepreneur","CEO / Executive","Creative Director","Tech Founder","Military Leader","Independent Consultant"],
    "famous":[{"name":"Steve Jobs","why":"Visionary who redefined personal computing"},{"name":"Martin Luther King Jr.","why":"Fearless leader who forged a new path for civil rights"},{"name":"Lady Gaga","why":"Constant artistic reinvention and unapologetic individuality"}],
    "forecast":"The universe has perfectly aligned your vibration with 2026 energy, promising massive breakthroughs, rapid career advancement, and a powerful shift into supreme leadership. Fortune strictly favors bold action this year.",
    "is_master":False},
  2:{"title":"The Diplomat","planet":"Moon","color":"White, Silver, Light Blue","colorHex":"#b8d4e8","day":"Monday",
    "overview":"Resonating intimately with lunar energy, Life Path 2s are the ultimate harmonizers of the world, gifted with profound near-psychic empathy and tactical diplomacy. Their core mission is to foster unity, though they must learn to assert their own boundaries to avoid being consumed by the pain of others.",
    "meta_desc":"Explore Life Path 2 meaning — The Diplomat. Personality traits, love compatibility, best careers, and your complete 2026 numerology forecast.",
    "strengths":["Exceptional empathic resonance","Masterful diplomatic negotiation","Meticulous detail-orientation","Profound intuitive understanding","Unshakable loyalty in partnerships"],
    "challenges":["A pervasive tendency toward codependency","Chronic avoidance of necessary conflict","Over-sensitivity to constructive criticism"],
    "love":"Deeply devoted, highly romantic, and incredibly nurturing — they crave absolute emotional security and total spiritual union. They thrive in harmonious partnerships but must guard against losing their individual identity to their lover.",
    "careers":["Counselor / Therapist","Mediator","Human Resources Director","Diplomat","Collaborative Artist","Support Specialist"],
    "famous":[{"name":"Barack Obama","why":"Diplomacy, dialogue, and unifying disparate groups"},{"name":"Jennifer Aniston","why":"Deeply empathetic, loyal, and harmonious screen presence"},{"name":"Kobe Bryant","why":"Deep dedication to team dynamics and long-term mentorship"}],
    "forecast":"The 2026 energy calls you to break free from past limitations, take bold emotional risks, and establish your own independent voice. Long-standing misunderstandings will find closure and partnerships will deepen significantly.",
    "is_master":False},
  3:{"title":"The Communicator","planet":"Jupiter","color":"Yellow, Gold, Cream","colorHex":"#e8d070","day":"Thursday",
    "overview":"Infused with Jupiterian expansion, the Life Path 3 acts as a dynamic vessel for joy, unbounded creativity, and expressive art. They navigate existence as a vibrant canvas, utilizing natural charisma to uplift the collective while striving to maintain disciplined focus amid their scattered brilliance.",
    "meta_desc":"Dive into Life Path 3 meaning — The Communicator. Personality, love compatibility, best careers, famous 3s, and your 2026 numerology forecast.",
    "strengths":["Magnetic and radiant charisma","Boundless creative imagination","Natural gift for all forms of expression","Infectious uplifting optimism","Exceptional social connection"],
    "challenges":["Scattered energy and procrastination","Difficulty completing long-term projects","Sensitivity to criticism"],
    "love":"Playful, highly affectionate, and easily bored — they absolutely require a partner who is intellectually stimulating and appreciative of their vibrant social life. Honest, open, and witty communication is their absolute non-negotiable.",
    "careers":["Writer / Author","Performer / Actor","Marketing Creative","Public Speaker","Content Creator","Graphic Designer"],
    "famous":[{"name":"David Bowie","why":"Ultimate chameleon of creative self-expression"},{"name":"Christina Aguilera","why":"Powerful vocal expression communicating deep emotion"},{"name":"Snoop Dogg","why":"Natural gift for language, entertainment, and social connectivity"}],
    "forecast":"An incredible influx of creative opportunities in 2026. Ideas that previously struggled will now find a receptive audience. The strategic imperative is absolute focus — channel your immense energy into one meaningful goal.",
    "is_master":False},
  4:{"title":"The Builder","planet":"Rahu","color":"Grey, Blue, Olive Green","colorHex":"#8899aa","day":"Wednesday",
    "overview":"Deeply grounded and highly disciplined, the Life Path 4 is the supreme architect of the numerological spectrum, possessing the unique ability to turn chaotic abstract ideas into lasting physical reality. Their karmic path requires mastering the material realm through meticulous hard work.",
    "meta_desc":"Learn about Life Path 4 meaning — The Builder. Core traits, best careers, love relationships, famous 4s, and your complete 2026 numerology forecast.",
    "strengths":["Exceptional organizational discipline","Unwavering reliability and loyalty","Masterful long-term strategic planning","Superior financial prudence","Tireless highly productive work ethic"],
    "challenges":["Rigid inflexibility and resistance to change","Pervasive pessimism under stress","Dangerous propensity for burnout"],
    "love":"They view romantic love as a vital stabilizing force and take commitment exceptionally seriously. Highly practical and fiercely protective, they express deep affection through acts of service and by building a secure foundation for their family.",
    "careers":["Architect / Engineer","Project Manager","Financial Analyst","Real Estate Professional","Systems Analyst","Legal Professional"],
    "famous":[{"name":"Elon Musk","why":"Building systemic foundations for a multi-planetary future"},{"name":"Oprah Winfrey","why":"Methodically constructed a media empire from nothing"},{"name":"Bill Gates","why":"Disciplined structured approach to building global systems"}],
    "forecast":"Your meticulous long-term hard work finally yields substantial rewards in 2026. The universe grants you cosmic permission to break the mold — unconventional new methodologies will open financial doors you did not know existed.",
    "is_master":False},
  5:{"title":"The Explorer","planet":"Mercury","color":"Green, Aqua Blue, White","colorHex":"#70c8b0","day":"Wednesday",
    "overview":"Intensely mercurial and constantly in kinetic motion, the Life Path 5 seeks absolute truth through lived experience, global travel, and varied sensory engagement. Their ultimate spiritual challenge is to find grounded discipline within their boundless freedom.",
    "meta_desc":"Discover Life Path 5 meaning — The Explorer. Personality traits, love compatibility, ideal careers, and your detailed 2026 numerology forecast.",
    "strengths":["Extremely high adaptability","Magnetic and persuasive charisma","Fearless and boundless curiosity","Exceptional resourcefulness in crisis","Highly persuasive quick communication"],
    "challenges":["Chronic restlessness and inconsistency","A deep-seated avoidance of commitment","Highly impulsive risky decision-making"],
    "love":"Exciting, highly unpredictable, and deeply passionate — they possess a core fear of being trapped and absolutely require a lover who is simultaneously an adventurous best friend. Relationships must continually evolve to survive the 5's need for variety.",
    "careers":["Travel Journalist","Digital Nomad Entrepreneur","Marketing Strategist","Sales Professional","Event Producer","Tech Explorer"],
    "famous":[{"name":"Angelina Jolie","why":"Fearless exploration of diverse roles, cultures, and causes"},{"name":"Abraham Lincoln","why":"Resourceful adaptability in the face of massive societal change"},{"name":"Mick Jagger","why":"Restless creative energy that refuses any form of containment"}],
    "forecast":"An exhilarating feast of unpredictable possibilities awaits you in 2026. Career prospects are incredibly favorable, particularly in digital and tech markets. The critical lesson is ruthless discernment — genuine opportunity vs. exciting distraction.",
    "is_master":False},
  6:{"title":"The Nurturer","planet":"Venus","color":"Pink, Peach, Rose Gold","colorHex":"#f0a0b8","day":"Friday",
    "overview":"Bathed in Venusian harmony, the Life Path 6 is driven by an innate unshakeable sense of duty, emotional healing, and the creation of aesthetic beauty. They are the cosmic parents of the world, tasked with learning the delicate balance between supporting others and maintaining their own energetic reserves.",
    "meta_desc":"Explore Life Path 6 meaning — The Nurturer. Personality, love compatibility, ideal careers, famous 6s, and your complete 2026 numerology forecast.",
    "strengths":["Profound and unwavering compassion","Natural talent for creating beauty and harmony","Exceptional conflict mediation skills","Deeply reliable responsibility","Magnetic community-building warmth"],
    "challenges":["Crippling martyrdom complex","Intrusive perfectionism about others lives","Dangerous susceptibility to emotional exhaustion"],
    "love":"Fiercely devoted and highly romantic, they tirelessly seek the ultimate harmonious domestic haven. They offer unconditional boundless support but possess exceptionally high expectations for mutual commitment, fidelity, and harmonious living.",
    "careers":["Counselor / Social Worker","Interior Designer","Hospitality Manager","Teacher / Educator","Healthcare Provider","Community Leader"],
    "famous":[{"name":"John Lennon","why":"Unwavering advocacy for universal love, harmony, and peace"},{"name":"Michael Jackson","why":"Devoted artistic nurturing and humanitarian philanthropy"},{"name":"Eleanor Roosevelt","why":"Tireless service as the ultimate community caretaker"}],
    "forecast":"Your immense power as a reliable emotional anchor is globally recognized in 2026. Tremendous good fortune in family and community dynamics is heralded. The greatest challenge is radical restructuring of old patterns and masterful boundary-setting.",
    "is_master":False},
  7:{"title":"The Seeker","planet":"Ketu","color":"Purple, Indigo, Grey","colorHex":"#9b6bbf","day":"Monday",
    "overview":"Operating on a highly intellectual and intensely mystical frequency, the Life Path 7 relentlessly seeks the absolute truth hidden beneath the surface of reality. Their unique journey perfectly marries strict empirical analysis with deep esoteric spiritual intuition.",
    "meta_desc":"Discover Life Path 7 meaning — The Seeker. Core traits, spiritual insights, best careers, love compatibility, and your 2026 numerology forecast.",
    "strengths":["Unmatched analytical genius","Profound highly accurate intuition","Advanced research proficiency","Immense philosophical depth","Keen penetrating observation skills"],
    "challenges":["Chronic cynicism and skepticism","A tendency toward social isolation","Constantly over-intellectualizing emotions"],
    "love":"Intensely private and notoriously hard to truly know, they require a profoundly deep intellectual and spiritual connection before opening their hearts. They absolutely must have a partner who respects their requirement for extensive quiet solitude.",
    "careers":["Research Scientist","Philosopher / Academic","Spiritual Teacher","Investigative Journalist","Data Analyst","Psychologist"],
    "famous":[{"name":"Nikola Tesla","why":"Relentless intellectual pursuit of hidden universal truths"},{"name":"Princess Diana","why":"Deep introspective empathy combined with intense spiritual seeking"},{"name":"Stephen Hawking","why":"Unmatched analytical genius probing the fundamental laws of reality"}],
    "forecast":"A potent period of deep spiritual awakening in 2026 that demands you transform introspective wisdom into bold active leadership. Trust your highly refined intuition as an absolute infallible compass.",
    "is_master":False},
  8:{"title":"The Powerhouse","planet":"Saturn","color":"Navy Blue, Black, Dark Grey","colorHex":"#334466","day":"Saturday",
    "overview":"Driven strictly by heavy Saturnian discipline, the Life Path 8 is the undisputed master of the material realm, uniquely tasked with navigating the ethical balanced use of massive power and wealth. They manifest vast success through relentless endurance, financial acumen, and highly strategic vision.",
    "meta_desc":"Learn about Life Path 8 meaning — The Powerhouse. Personality traits, best careers, love compatibility, famous 8s, and your 2026 numerology forecast.",
    "strengths":["Extraordinary executive authority","Unparalleled financial acumen","Relentless endurance under pressure","Superior strategic long-term vision","Commanding and highly magnetic presence"],
    "challenges":["Destructive workaholism","Materialistic obsession","Dictatorial tendencies under stress"],
    "love":"Intense, highly demanding, and fiercely loyal, they approach romantic relationships with the exact same strategic seriousness as their corporate careers. They actively seek a powerful equal partner with whom they can build and secure a formidable legacy.",
    "careers":["CEO / Business Owner","Investment Banker","Corporate Executive","Real Estate Developer","Attorney","Financial Strategist"],
    "famous":[{"name":"Oprah Winfrey","why":"Built a formidable media empire through sheer Saturnian discipline"},{"name":"Pablo Picasso","why":"Masterful disciplined accumulation of artistic power and legacy"},{"name":"Nelson Mandela","why":"Extraordinary endurance and strategic vision under immense pressure"}],
    "forecast":"An incredibly strong karmic year for financial and career dominance in 2026. Business investments, massive promotions, and unprecedented breakthroughs are highly indicated. Remain strategically adaptable and embrace novel opportunities.",
    "is_master":False},
  9:{"title":"The Humanitarian","planet":"Mars","color":"Red, Maroon, Coral","colorHex":"#c84848","day":"Tuesday",
    "overview":"Embodying the absolute culmination of the human experience, the Life Path 9 operates on a highly elevated global consciousness, driven by raw martial energy to fight for the greater good. Their ultimate spiritual lesson involves mastering total forgiveness and releasing deep attachment to the past.",
    "meta_desc":"Explore Life Path 9 meaning — The Humanitarian. Core traits, love compatibility, ideal careers, famous 9s, and your complete 2026 numerology forecast.",
    "strengths":["Truly universal and expansive compassion","Profound philosophical and spiritual wisdom","Immense natural generosity","Powerful and inspiring global vision","Exceptional artistic and creative talent"],
    "challenges":["Deep resentment of the past","Emotional naivety regarding others motives","Tendency to self-sacrifice to a destructive fault"],
    "love":"Deeply romantic, highly idealistic, and intensely giving — they love universally and occasionally struggle to focus their vast emotional energy solely on one person. They require a partner who shares their high idealism and humanitarian worldview.",
    "careers":["Non-profit Leader","Artist / Musician","Humanitarian Worker","Spiritual Teacher","Healer / Therapist","Social Activist"],
    "famous":[{"name":"Mahatma Gandhi","why":"Embodied pure universal compassion and tireless humanitarian sacrifice"},{"name":"Jim Carrey","why":"Used creative brilliance to explore profound existential and spiritual themes"},{"name":"Morgan Freeman","why":"Wise philosophical presence communicating universal human truths"}],
    "forecast":"A profound transformative period of karmic release and renewal in 2026. Old cycles will gracefully end. Once these heavy burdens are released, highly aligned new opportunities will flow in with startling ease.",
    "is_master":False},
  11:{"title":"The Spiritual Messenger","planet":"Moon (Master)","color":"Silver, Pearl, Indigo","colorHex":"#a0a8c8","day":"Monday",
    "overview":"As the first Master Number, the 11 operates as a highly sensitive cosmic antenna, constantly receiving profound psychic and intuitive insights from higher realms. Their ultimate mission is to uplift humanity through visionary illumination.",
    "meta_desc":"Discover Life Path 11 meaning — The Spiritual Messenger. Master Number traits, intuition, love, careers, and your powerful 2026 numerology forecast.",
    "strengths":["Extraordinary psychic-level intuition","Highly elevated spiritual awareness","Visionary illumination for humanity","Immense creative inspiration","Deep empathic resonance"],
    "challenges":["Extreme nervous tension and severe anxiety","Crippling self-doubt","Frequent debilitating emotional overwhelm"],
    "love":"They desperately seek a transcendent soul-mate connection and feel love with agonizing consuming intensity. They require an incredibly patient, grounded partner who understands their sudden non-negotiable needs for complete isolation.",
    "careers":["Spiritual Teacher","Healer / Energy Worker","Visionary Artist","Psychologist","Inspirational Speaker","Metaphysical Researcher"],
    "famous":[{"name":"Barack Obama","why":"Illuminating visionary leadership bridging diverse human experiences"},{"name":"Edgar Allan Poe","why":"Profoundly psychic creative vision exploring the darkest human depths"},{"name":"Wolfgang Amadeus Mozart","why":"Divine musical channeling that transcended ordinary human perception"}],
    "forecast":"Your heightened intuition is your absolute compass in 2026. Astrologically empowered to unite disparate forces and orchestrate profound visionary changes in your wider community.",
    "is_master":True},
  22:{"title":"The Master Builder","planet":"Rahu (Master)","color":"Coral, Copper, Gold","colorHex":"#c87848","day":"Sunday",
    "overview":"The Master Number 22 possesses the extraordinary ability to ground immense ethereal spiritual visions into lasting highly functional material empires. Tasked with building complex systemic legacies that will vastly outlast them.",
    "meta_desc":"Learn about Life Path 22 meaning — The Master Builder. Master Number traits, manifesting power, love, careers, and your 2026 numerology forecast.",
    "strengths":["Unparalleled practical manifesting ability","Extraordinary large-scale visionary capacity","Supreme organizational and systemic mastery","Immense psychological endurance","Rare combination of idealism and pragmatism"],
    "challenges":["Crippling fear of failure","Severe inflexibility with subordinates","Autocratic behavior under extreme stress"],
    "love":"Fiercely loyal and profoundly protective, they demonstrate romantic love by providing an unshakeable highly secure material foundation. Their partners absolutely must be highly self-sufficient.",
    "careers":["Visionary Architect","Global Non-Profit Leader","Tech Empire Founder","Political Reformer","Master Engineer","Transformational Business Builder"],
    "famous":[{"name":"Bill Gates","why":"Built a global empire that systemically transformed human access to technology"},{"name":"Dalai Lama","why":"Masterfully builds bridges of compassionate global understanding"},{"name":"Paul McCartney","why":"Constructed a vast enduring cultural legacy"}],
    "forecast":"A monumental foundational year in 2026 where groundwork of the past perfectly aligns. Lead with deep compassion rather than ruthless mechanical efficiency to unlock your full potential.",
    "is_master":True},
  33:{"title":"The Master Teacher","planet":"Venus (Master)","color":"White, Pale Yellow, Pearl","colorHex":"#f0e8c8","day":"Friday",
    "overview":"The extremely rare Master Number 33 vibrates with pure unconditional love and divine compassion, operating as an unwavering beacon of spiritual guidance for the masses. Their immense empathic burden requires mastering the art of radical self-preservation.",
    "meta_desc":"Explore Life Path 33 meaning — The Master Teacher. Rarest Master Number traits, unconditional love, ideal careers, and your 2026 numerology forecast.",
    "strengths":["Radiating unconditional divine love","Extraordinary selfless service capacity","Profound multi-generational healing wisdom","Natural beacon of spiritual guidance","Supreme compassionate empathy"],
    "challenges":["Extreme highly destructive self-sacrifice","Chronic severe energetic depletion","Assuming inappropriate responsibility for others karma"],
    "love":"The ultimate selfless caregivers in romance, offering a love that is highly protective, deeply nurturing, and spiritually elevated. They must consciously avoid treating romantic partners as broken projects that need to be healed.",
    "careers":["Spiritual Healer","Master Teacher / Educator","Universal Compassion Activist","Holistic Health Practitioner","Sacred Arts Creator","Global Humanitarian"],
    "famous":[{"name":"Albert Einstein","why":"Universal compassion through transformative contributions to collective human understanding"},{"name":"Meryl Streep","why":"Profoundly empathetic artistic channeling of the full spectrum of human experience"},{"name":"Francis of Assisi","why":"Embodied absolute selfless divine love and total compassionate sacrifice"}],
    "forecast":"Rigorous radical self-care is absolutely non-negotiable in 2026. Prevent burnout by fiercely prioritizing yourself first, ensuring you seize your own emerging powerful doors of opportunity.",
    "is_master":True},
}

COMPAT = {
  "1-1":{"score":65,"label":"Twin Flames or Ego Clash","desc":"Two pioneers in one room — either you build an empire together or battle for the throne. Requires immense psychological maturity to avoid territorial disputes."},
  "1-2":{"score":62,"label":"Leadership Meets Sensitivity","desc":"The 1's directness often feels abrasive to the 2's sensitive nature. Deep love is possible, but the 2 must assert their needs and the 1 must learn to listen."},
  "1-3":{"score":82,"label":"Magnetic Spark","desc":"Sun meets Jupiter — a powerful, creative partnership. The 3's joyful expression perfectly complements the 1's bold vision. High energy, high compatibility."},
  "1-4":{"score":52,"label":"Vision vs Structure","desc":"The 1's rapid forward motion clashes with the 4's methodical pace. Shared goals can bridge the gap, but patience is absolutely required from both sides."},
  "1-5":{"score":85,"label":"Dynamic Freedom Partnership","desc":"Two fiercely independent souls who understand each other's need for space. Fast-moving, exciting, and mutually inspiring. One of the most naturally compatible pairings."},
  "1-6":{"score":68,"label":"Leader and Nurturer","desc":"The 6's devotion beautifully supports the 1's ambitions. However, the 1 must be careful not to neglect the 6's deep need for reciprocal affection."},
  "1-7":{"score":70,"label":"Action Meets Contemplation","desc":"An intriguing pairing of opposite energies. The 1 acts while the 7 reflects. With mutual respect for each other's pace, this can be a deeply enriching connection."},
  "1-8":{"score":48,"label":"Power Struggle","desc":"The Sun and Saturn are planetary enemies. Two dominant forces, both demanding ultimate authority. This pairing requires exceptional psychological maturity and shared purpose."},
  "1-9":{"score":75,"label":"Warrior Alliance","desc":"Both are driven by purpose. The 1 pioneers the path; the 9 envisions the destination. A powerful partnership provided their causes align."},
  "2-2":{"score":78,"label":"Emotional Mirror","desc":"Deep mutual understanding and immense sensitivity. Beautiful harmony is possible, but both must work hard to avoid codependency."},
  "2-3":{"score":84,"label":"Harmony and Expression","desc":"The 2 provides a stable, appreciative audience for the 3's creative outpouring. A vibrant, emotionally rich, and socially engaging partnership."},
  "2-4":{"score":80,"label":"Stable Foundation","desc":"Moon and Rahu create a grounded, reliable union. The emotional diplomat is securely anchored by the pragmatic builder — a beautiful, enduring combination."},
  "2-5":{"score":52,"label":"Stability vs Freedom","desc":"The 5's erratic adventure-seeking triggers the 2's deep abandonment fears. Requires constant negotiation and exceptional mutual patience."},
  "2-6":{"score":88,"label":"Divine Harmony","desc":"The absolute pinnacle of compatibility. Moon meets Venus — profound emotional understanding, mutual caretaking, and a gentleness that allows both partners to flourish fully."},
  "2-7":{"score":65,"label":"Emotional vs Analytical","desc":"The 2 craves emotional merging while the 7 requires intellectual solitude. Can be deeply enriching if the 2 respects the 7's sacred need for independent space."},
  "2-8":{"score":55,"label":"Heart vs Ambition","desc":"Saturn is a planetary enemy of the Moon. The 8's intense ambition often cools the 2's emotional warmth into a state of isolated coldness."},
  "2-9":{"score":72,"label":"Compassionate Souls","desc":"Both are deeply devoted to others. A loving, service-oriented partnership, though the 9's broad humanitarian focus may sometimes leave the 2 feeling personally neglected."},
  "3-3":{"score":74,"label":"Creative Explosion","desc":"A spectacular burst of creative energy and social joy. However, both share the same scattered tendencies — grounding mechanisms are essential for long-term stability."},
  "3-4":{"score":48,"label":"Freedom vs Structure","desc":"The 4's rigid need for predictable foundations feels like a psychological prison to the 3. The 3's scattered nature incites deep anxiety in the 4."},
  "3-5":{"score":80,"label":"Adventure Partners","desc":"One of the most exciting and energetic combinations. Shared adventures, intellectual partnership, and rapid verbal exchange. An endlessly stimulating pairing."},
  "3-6":{"score":83,"label":"Joyful Harmony","desc":"Both share a profound appreciation for aesthetics, pleasure, and social harmony. A joyful, family-creative unit with mutual appreciation for beauty."},
  "3-7":{"score":55,"label":"Optimism vs Depth","desc":"The 3's extroverted optimism often rings hollow to the deeply introspective 7. An intellectually stimulating pairing if both can appreciate their different processing styles."},
  "3-8":{"score":50,"label":"Creativity vs Ambition","desc":"The 3's creative spontaneity frequently clashes with the 8's rigid, goal-oriented structure. Both must make significant intentional compromises."},
  "3-9":{"score":79,"label":"Inspirational Union","desc":"Jupiter's expansion meets Mars's idealism. A deeply inspirational partnership focused on uplifting the collective. Both share a love for culture and global impact."},
  "4-4":{"score":76,"label":"Solid Rock Partnership","desc":"Two builders building together — exceptional stability, shared values, and mutual respect for hard work. Watch for combined stubbornness creating immovable stalemates."},
  "4-5":{"score":45,"label":"Walls vs Wings","desc":"The lowest overall compatibility pairing. The 4 builds walls for security while the 5 views those exact walls as a threat to their autonomy."},
  "4-6":{"score":80,"label":"Security and Devotion","desc":"The ultimate traditional family foundation. The 4 provides structure and security while the 6 transforms that stability into a warm, beautiful, nurturing home."},
  "4-7":{"score":82,"label":"Grounded Seeker","desc":"An excellent karmic axis. The practical builder successfully grounds the cerebral seeker, providing the 7 with the secure base needed to explore spiritual realms."},
  "4-8":{"score":90,"label":"Power Couple","desc":"The single most compatible combination in all of numerological synastry. Both understand the intrinsic value of hard work, delayed gratification, and material foundations."},
  "4-9":{"score":52,"label":"Pragmatism vs Idealism","desc":"The 4's pragmatic self-security focus clashes directly with the 9's willingness to sacrifice resources for the humanitarian collective."},
  "5-5":{"score":70,"label":"Double Freedom","desc":"Two explorers exploring together — electrifying adventures and shared excitement. However, the combined lack of stability can make this feel like a perpetual vacation with no home base."},
  "5-6":{"score":52,"label":"Freedom vs Home","desc":"The 6's intense nurturing duty feels suffocating to the 5, while the 5's unpredictability chronically triggers the 6's deep domestic anxieties."},
  "5-7":{"score":73,"label":"Independent Intellectuals","desc":"Both value non-traditional relationship structures and individual exploration. Mutual respect creates a deeply stimulating intellectual depth."},
  "5-8":{"score":55,"label":"Speed vs Control","desc":"Mercury's fast, erratic speed operates in direct opposition to Saturn's slow, methodical, and controlling nature."},
  "5-9":{"score":72,"label":"Freedom Seekers","desc":"Both value independence and resist being caged by convention. An exciting, adventurous partnership with shared appreciation for global exploration."},
  "6-6":{"score":80,"label":"Twin Nurturers","desc":"Extraordinarily harmonious — two Venusian nurturers creating a beautiful home together. The risk is over-caretaking each other while neglecting individual growth."},
  "6-7":{"score":55,"label":"Togetherness vs Solitude","desc":"The 6's desire for constant domestic intimacy deeply intrudes upon the 7's sacred need for psychological solitude, creating a painful cycle of pursuit and retreat."},
  "6-8":{"score":74,"label":"Heart and Power","desc":"The 8 provides the material resources while the 6 transforms those resources into a beautiful, nurturing home. A synergistic and highly functional pairing."},
  "6-9":{"score":80,"label":"Universal Love","desc":"The micro-caretaker meets the macro-caretaker. A partnership of immense compassion, shared ideals, and a beautiful home life that naturally becomes a beacon for others."},
  "7-7":{"score":72,"label":"Twin Seekers","desc":"Two highly independent intellectuals and philosophical searchers. Deeply stimulating and profoundly understood by one another, but susceptible to emotional distance."},
  "7-8":{"score":60,"label":"Spirit vs Matter","desc":"The 7's spiritual depth can feel alien to the 8's material focus. However, if the 8 values wisdom and the 7 appreciates ambition, this can achieve an unusual balance."},
  "7-9":{"score":62,"label":"Wisdom Seekers","desc":"The 9's extroverted collective-focused energy exhausts the 7's limited social battery. Both must consciously honor each other's fundamentally different social needs."},
  "8-8":{"score":68,"label":"Corporate Empire","desc":"Two powerful, highly ambitious forces. Can build extraordinary material success together, but must be vigilant against a cold, competitive atmosphere."},
  "8-9":{"score":52,"label":"Material vs Spiritual","desc":"A collision of core values. The 8 accumulates wealth through logic while the 9 sacrifices it for ideals. To the 9 the 8 appears ruthless; to the 8 the 9 appears naive."},
  "9-9":{"score":78,"label":"Humanitarian Alliance","desc":"Two humanitarians on a shared world-saving mission. An inspiring, deeply purposeful partnership — both must ensure their vast love for the collective also flows toward each other."},
}

def get_compat(a, b):
    k1 = f"{min(a,b)}-{max(a,b)}"
    return COMPAT.get(k1, {"score":65,"label":"Unique Connection","desc":"Your combination is rare. What matters most is the conscious effort both of you bring to understanding each other's deeply different energetic rhythms."})

def score_color(score):
    if score >= 80: return "#1D9E75"
    if score >= 65: return "#c9a96e"
    return "#c84848"

def score_label(score):
    if score >= 85: return "Highly Compatible"
    if score >= 75: return "Well Matched"
    if score >= 65: return "Can Work With Effort"
    return "Challenging — But Growth-Oriented"

# ─── HTML Template: Meaning Page ────────────────────────
def meaning_page(n, d):
    master_badge = '<span style="display:inline-flex;align-items:center;gap:5px;background:linear-gradient(135deg,rgba(155,107,191,.15),rgba(196,160,224,.15));border:1px solid rgba(155,107,191,.3);border-radius:99px;padding:4px 12px;font-size:11px;color:#9b6bbf;font-weight:500;margin-bottom:12px;margin-left:8px;">✦ Master Number</span>' if d["is_master"] else ""
    strengths_html = "\n".join([f'<li style="margin-bottom:6px;color:#6b5744;">✦ {s}</li>' for s in d["strengths"]])
    challenges_html = "\n".join([f'<li style="margin-bottom:6px;color:#6b5744;">◦ {c}</li>' for c in d["challenges"]])
    careers_html = "\n".join([f'<span style="display:inline-block;background:rgba(255,255,255,.7);border:1px solid rgba(201,169,110,.2);border-radius:99px;padding:5px 14px;font-size:12.5px;color:#6b5744;margin:3px;">{c}</span>' for c in d["careers"]])
    famous_html = "\n".join([f'<div style="background:rgba(255,255,255,.6);border:1px solid rgba(201,169,110,.18);border-radius:10px;padding:8px 12px;margin:4px 0;"><strong style="font-size:13px;color:#2d2418;display:block;">{f["name"]}</strong><span style="font-size:12px;color:#a08878;">{f["why"]}</span></div>' for f in d["famous"]])

    # Related numbers
    nums = [1,2,3,4,5,6,7,8,9,11,22,33]
    others = [x for x in nums if x != n]
    related_html = "\n".join([f'<a href="/life-path-{x}-meaning/" style="display:inline-block;background:rgba(255,255,255,.6);border:1px solid rgba(201,169,110,.2);border-radius:10px;padding:8px 12px;text-align:center;text-decoration:none;margin:4px;min-width:60px;"><span style="font-family:Playfair Display,serif;font-size:18px;font-weight:700;color:{DATA[x]["colorHex"]};display:block;">{x}</span><span style="font-size:10px;color:#a08878;">{DATA[x]["title"].replace("The ","")}</span></a>' for x in others])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Life Path {n} Meaning — {d["title"]} | Lumina Numbers</title>
<meta name="description" content="{d["meta_desc"]}">
<meta property="og:title" content="Life Path {n} — {d["title"]} | Lumina Numbers">
<meta property="og:description" content="{d["meta_desc"]}">
<meta property="og:image" content="/og-image.jpg">
<link rel="canonical" href="https://luminanumbers.com/life-path-{n}-meaning/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="/js/cookie-consent.js" data-ga="G-LSCWW3E9XV"></script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--cream:#fdf8f2;--gold:#c9a96e;--gold-light:#e8d5b0;--peach:#f5c4a8;--text-dark:#2d2418;--text-mid:#6b5744;--text-soft:#a08878;--glass:rgba(255,255,255,0.6);--glass-border:rgba(201,169,110,0.22);--shadow:0 8px 32px rgba(180,140,100,0.13)}}
html{{scroll-behavior:smooth}}
body{{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--text-dark);overflow-x:hidden;-webkit-font-smoothing:antialiased}}
.bg-aura{{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse 80% 60% at 70% 10%,rgba(232,213,176,.4) 0%,transparent 60%),radial-gradient(ellipse 55% 50% at 15% 80%,rgba(212,191,232,.32) 0%,transparent 55%),var(--cream)}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 5vw;height:64px;background:rgba(253,248,242,.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(201,169,110,.13)}}
.nav-logo{{display:flex;align-items:center;gap:9px;text-decoration:none}}
.nav-logo-icon{{width:32px;height:32px;background:linear-gradient(135deg,#e8d5b0,#c9a96e);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px}}
.nav-logo-name{{font-family:'Playfair Display',serif;font-size:15px;font-weight:600;color:#2d2418;letter-spacing:.07em}}
.nav-logo-sub{{font-size:9px;letter-spacing:.1em;color:#c9a96e;text-transform:uppercase}}
.nav-back{{font-size:13px;color:#a08878;text-decoration:none;transition:color .2s}}
.nav-back:hover{{color:#c9a96e}}
.hero{{position:relative;z-index:1;padding:88px 5vw 40px;text-align:center;max-width:800px;margin:0 auto}}
.eyebrow{{font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-bottom:12px;display:flex;align-items:center;justify-content:center;gap:8px}}
.eyebrow::before,.eyebrow::after{{content:'✦';font-size:9px}}
.lp-number{{font-family:'Playfair Display',serif;font-size:clamp(80px,18vw,120px);font-weight:700;line-height:1;color:{d["colorHex"]};margin-bottom:8px;{f"background:linear-gradient(135deg,#9b6bbf,#c4a0e0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;" if d["is_master"] else ""}}}
h1{{font-family:'Playfair Display',serif;font-size:clamp(28px,5vw,48px);line-height:1.15;color:#2d2418;margin-bottom:8px}}
.hero-sub{{font-size:15px;color:#a08878;line-height:1.65;max-width:580px;margin:0 auto 0}}
.color-info{{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px;flex-wrap:wrap}}
.color-dot{{width:16px;height:16px;border-radius:50%;background:{d["colorHex"]};border:2px solid rgba(255,255,255,.7)}}
.info-pill{{background:rgba(255,255,255,.6);border:1px solid rgba(201,169,110,.2);border-radius:99px;padding:4px 12px;font-size:12px;color:#6b5744}}
.content{{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:32px 5vw 80px}}
.card{{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow)}}
.card-title{{font-family:'Playfair Display',serif;font-size:17px;font-weight:600;color:#2d2418;margin-bottom:14px;display:flex;align-items:center;gap:8px}}
.card-text{{font-size:14px;color:#6b5744;line-height:1.8}}
.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
.forecast-card{{background:linear-gradient(135deg,rgba(201,169,110,.15),rgba(245,196,168,.15));border:1px solid rgba(201,169,110,.25);border-radius:20px;padding:24px;margin-bottom:16px}}
.forecast-year{{font-size:12px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:var(--gold);margin-bottom:8px}}
.cta-card{{background:linear-gradient(135deg,rgba(245,196,168,.3),rgba(212,191,232,.3));border:1px solid rgba(201,169,110,.2);border-radius:20px;padding:28px;margin-bottom:16px;text-align:center}}
.btn-cta{{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,#f5c4a8,#c9a96e);color:white;border:none;border-radius:14px;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;cursor:pointer;text-decoration:none;box-shadow:0 6px 20px rgba(201,169,110,.4);transition:transform .15s}}
.btn-cta:hover{{transform:translateY(-2px)}}
@media(max-width:600px){{.two-col{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="bg-aura"></div>
<nav>
  <a href="/" class="nav-logo">
    <div class="nav-logo-icon">✦</div>
    <div>
      <div class="nav-logo-name">LUMINA NUMBERS</div>
      <div class="nav-logo-sub">Discover Your Divine Numbers</div>
    </div>
  </a>
  <a href="/" class="nav-back">← Home</a>
</nav>

<div class="hero">
  <div class="eyebrow">Life Path Number {n}</div>
  <div class="lp-number">{n}</div>
  {master_badge}
  <h1>{d["title"]}</h1>
  <p class="hero-sub">Governed by {d["planet"]} · Lucky Day: {d["day"]}</p>
  <div class="color-info">
    <div class="color-dot"></div>
    <span class="info-pill">🎨 {d["color"]}</span>
    <span class="info-pill">🪐 {d["planet"]}</span>
    <span class="info-pill">📅 {d["day"]}</span>
  </div>
</div>

<div class="content">

  <div class="card">
    <div class="card-title">✨ Overview</div>
    <p class="card-text">{d["overview"]}</p>
  </div>

  <div class="two-col">
    <div class="card">
      <div class="card-title">💪 Core Strengths</div>
      <ul style="list-style:none;padding:0">{strengths_html}</ul>
    </div>
    <div class="card">
      <div class="card-title">🌱 Key Challenges</div>
      <ul style="list-style:none;padding:0">{challenges_html}</ul>
    </div>
  </div>

  <div class="card" style="background:linear-gradient(135deg,rgba(232,164,176,.18),rgba(212,191,232,.18));border-color:rgba(232,164,176,.28);">
    <div class="card-title">♡ Love &amp; Relationships</div>
    <p class="card-text">{d["love"]}</p>
  </div>

  <div class="card">
    <div class="card-title">💼 Ideal Careers</div>
    <div style="margin-top:4px">{careers_html}</div>
  </div>

  <div class="card">
    <div class="card-title">⭐ Famous Life Path {n}s</div>
    {famous_html}
  </div>

  <div class="forecast-card">
    <div class="forecast-year">✦ 2026 Numerology Forecast · Universal Year 1</div>
    <p class="card-text">{d["forecast"]}</p>
  </div>

  <div class="cta-card">
    <div style="font-family:'Playfair Display',serif;font-size:22px;font-weight:600;color:#2d2418;margin-bottom:8px;">Calculate Your Life Path Number</div>
    <p style="font-size:14px;color:#a08878;margin-bottom:20px;">Enter your birth date to confirm your Life Path and get your complete personal reading.</p>
    <a href="/life-path-calculator/" class="btn-cta">✦ Get My Full Reading →</a>
  </div>

  <div class="card">
    <div class="card-title">🔢 Explore All Life Path Numbers</div>
    <div style="margin-top:8px">{related_html}</div>
  </div>

</div>
</body>
</html>"""

# ─── HTML Template: Compatibility Page ──────────────────
def compat_page(n1, n2, c, d1, d2):
    pct_color = score_color(c["score"])
    pct_label = score_label(c["score"])
    bar_w = c["score"]

    # Tips per score
    if c["score"] >= 80:
        tips = ["Lean into your natural harmony and build shared rituals together","Celebrate what makes you different — it is your greatest strength","This pairing thrives when both partners maintain individual passions"]
    elif c["score"] >= 65:
        tips = ["Schedule regular honest conversations about needs and boundaries","Appreciate that your differences create balance, not conflict","Practice patience — your rhythms are different but compatible"]
    else:
        tips = ["Focus on shared values rather than surface-level differences","Give each other generous amounts of space and independence","Seek to understand before seeking to be understood"]

    tips_html = "\n".join([f'<li style="margin-bottom:8px;color:#6b5744;font-size:14px;">✦ {t}</li>' for t in tips])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Life Path {n1} and {n2} Compatibility | Lumina Numbers</title>
<meta name="description" content="Explore Life Path {n1} and {n2} compatibility. {d1['title']} meets {d2['title']} — discover your natural compatibility score, strengths, and relationship insights.">
<meta property="og:title" content="Life Path {n1} and {n2} Compatibility | Lumina Numbers">
<meta property="og:image" content="/og-image.jpg">
<link rel="canonical" href="https://luminanumbers.com/life-path-{n1}-and-{n2}-compatibility/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="/js/cookie-consent.js" data-ga="G-LSCWW3E9XV"></script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--cream:#fdf8f2;--gold:#c9a96e;--text-dark:#2d2418;--text-mid:#6b5744;--text-soft:#a08878;--glass:rgba(255,255,255,0.6);--glass-border:rgba(201,169,110,0.22);--shadow:0 8px 32px rgba(180,140,100,0.13)}}
body{{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--text-dark);overflow-x:hidden;-webkit-font-smoothing:antialiased}}
.bg-aura{{position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse 80% 60% at 70% 10%,rgba(232,213,176,.4) 0%,transparent 60%),radial-gradient(ellipse 55% 50% at 15% 80%,rgba(212,191,232,.32) 0%,transparent 55%),var(--cream)}}
nav{{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:0 5vw;height:64px;background:rgba(253,248,242,.85);backdrop-filter:blur(16px);border-bottom:1px solid rgba(201,169,110,.13)}}
.nav-logo{{display:flex;align-items:center;gap:9px;text-decoration:none}}
.nav-logo-icon{{width:32px;height:32px;background:linear-gradient(135deg,#e8d5b0,#c9a96e);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px}}
.nav-logo-name{{font-family:'Playfair Display',serif;font-size:15px;font-weight:600;color:#2d2418;letter-spacing:.07em}}
.nav-logo-sub{{font-size:9px;letter-spacing:.1em;color:#c9a96e;text-transform:uppercase}}
.nav-back{{font-size:13px;color:#a08878;text-decoration:none;transition:color .2s}}
.nav-back:hover{{color:#c9a96e}}
.hero{{position:relative;z-index:1;padding:88px 5vw 40px;text-align:center;max-width:800px;margin:0 auto}}
.eyebrow{{font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-bottom:16px;display:flex;align-items:center;justify-content:center;gap:8px}}
.eyebrow::before,.eyebrow::after{{content:'✦';font-size:9px}}
.num-pair{{display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:12px}}
.np-num{{font-family:'Playfair Display',serif;font-size:clamp(56px,14vw,88px);font-weight:700;line-height:1}}
.np-x{{font-size:32px;color:#a08878;margin-top:8px}}
h1{{font-family:'Playfair Display',serif;font-size:clamp(22px,4vw,36px);color:#2d2418;margin-bottom:8px;line-height:1.2}}
.hero-sub{{font-size:14px;color:#a08878;line-height:1.65;max-width:540px;margin:0 auto}}
.content{{position:relative;z-index:1;max-width:800px;margin:0 auto;padding:32px 5vw 80px}}
.score-card{{background:linear-gradient(135deg,rgba(245,196,168,.3),rgba(212,191,232,.3));border:1px solid rgba(201,169,110,.22);border-radius:24px;padding:28px;margin-bottom:16px;text-align:center}}
.score-num{{font-family:'Playfair Display',serif;font-size:72px;font-weight:700;line-height:1;color:{pct_color}}}
.score-pct{{font-size:28px}}
.score-title{{font-family:'Playfair Display',serif;font-size:22px;color:#2d2418;margin:8px 0 4px}}
.score-sub{{font-size:13px;color:#a08878}}
.bar-wrap{{background:rgba(201,169,110,.15);border-radius:99px;height:10px;margin:16px 0 8px;overflow:hidden}}
.bar-fill{{height:100%;border-radius:99px;background:linear-gradient(90deg,#f5c4a8,{pct_color});width:{bar_w}%;transition:width 1s}}
.card{{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow)}}
.card-title{{font-family:'Playfair Display',serif;font-size:17px;font-weight:600;color:#2d2418;margin-bottom:12px;display:flex;align-items:center;gap:8px}}
.card-text{{font-size:14px;color:#6b5744;line-height:1.8}}
.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}}
.profile-card{{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:20px;text-align:center}}
.cta-card{{background:linear-gradient(135deg,rgba(245,196,168,.3),rgba(212,191,232,.3));border:1px solid rgba(201,169,110,.2);border-radius:20px;padding:28px;margin-bottom:16px;text-align:center}}
.btn-cta{{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,#f5c4a8,#c9a96e);color:white;border:none;border-radius:14px;padding:14px 28px;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;cursor:pointer;text-decoration:none;box-shadow:0 6px 20px rgba(201,169,110,.4);transition:transform .15s}}
.btn-cta:hover{{transform:translateY(-2px)}}
@media(max-width:600px){{.two-col{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="bg-aura"></div>
<nav>
  <a href="/" class="nav-logo">
    <div class="nav-logo-icon">✦</div>
    <div>
      <div class="nav-logo-name">LUMINA NUMBERS</div>
      <div class="nav-logo-sub">Discover Your Divine Numbers</div>
    </div>
  </a>
  <a href="/" class="nav-back">← Home</a>
</nav>

<div class="hero">
  <div class="eyebrow">Numerology Compatibility</div>
  <div class="num-pair">
    <span class="np-num" style="color:{d1['colorHex']}">{n1}</span>
    <span class="np-x">&amp;</span>
    <span class="np-num" style="color:{d2['colorHex']}">{n2}</span>
  </div>
  <h1>Life Path {n1} and {n2} Compatibility<br><em style="font-style:italic;color:#c9a96e;">{c["label"]}</em></h1>
  <p class="hero-sub">{d1["title"]} meets {d2["title"]} — a {score_label(c["score"]).lower()} pairing</p>
</div>

<div class="content">

  <div class="score-card">
    <div class="score-num">{c["score"]}<span class="score-pct">%</span></div>
    <div class="score-title">{c["label"]}</div>
    <div class="score-sub">{pct_label}</div>
    <div class="bar-wrap"><div class="bar-fill"></div></div>
  </div>

  <div class="card">
    <div class="card-title">💞 Relationship Dynamics</div>
    <p class="card-text">{c["desc"]}</p>
  </div>

  <div class="two-col">
    <div class="profile-card">
      <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:{d1['colorHex']};line-height:1;margin-bottom:8px">{n1}</div>
      <div style="font-family:'Playfair Display',serif;font-size:16px;color:#2d2418;margin-bottom:6px">{d1["title"]}</div>
      <div style="font-size:12px;color:#a08878">{d1["planet"]} · {d1["day"]}</div>
      <div style="font-size:13px;color:#6b5744;margin-top:10px;line-height:1.6">{d1["overview"][:160]}...</div>
      <a href="/life-path-{n1}-meaning/" style="display:inline-block;margin-top:12px;font-size:12px;color:#c9a96e;text-decoration:none;">Full Profile →</a>
    </div>
    <div class="profile-card">
      <div style="font-family:'Playfair Display',serif;font-size:40px;font-weight:700;color:{d2['colorHex']};line-height:1;margin-bottom:8px">{n2}</div>
      <div style="font-family:'Playfair Display',serif;font-size:16px;color:#2d2418;margin-bottom:6px">{d2["title"]}</div>
      <div style="font-size:12px;color:#a08878">{d2["planet"]} · {d2["day"]}</div>
      <div style="font-size:13px;color:#6b5744;margin-top:10px;line-height:1.6">{d2["overview"][:160]}...</div>
      <a href="/life-path-{n2}-meaning/" style="display:inline-block;margin-top:12px;font-size:12px;color:#c9a96e;text-decoration:none;">Full Profile →</a>
    </div>
  </div>

  <div class="card">
    <div class="card-title">✦ Relationship Tips</div>
    <ul style="list-style:none;padding:0">{tips_html}</ul>
  </div>

  <div class="cta-card">
    <div style="font-family:'Playfair Display',serif;font-size:20px;font-weight:600;color:#2d2418;margin-bottom:8px;">Check Your Exact Compatibility</div>
    <p style="font-size:14px;color:#a08878;margin-bottom:20px;">Enter both birth dates for a complete compatibility reading with Combination Code analysis.</p>
    <a href="/life-path-calculator/" class="btn-cta">✦ Calculate Compatibility →</a>
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

# Meaning pages
print("Generating meaning pages...")
for n, d in DATA.items():
    folder = os.path.join(BASE, f"life-path-{n}-meaning")
    make_dir(folder)
    write(os.path.join(folder, "index.html"), meaning_page(n, d))
    print(f"  ✦ /life-path-{n}-meaning/")
    count += 1

# Compatibility pages
print("\nGenerating compatibility pages...")
nums = list(DATA.keys())
for i in range(len(nums)):
    for j in range(i, len(nums)):
        n1, n2 = nums[i], nums[j]
        c = get_compat(n1, n2)
        d1, d2 = DATA[n1], DATA[n2]
        folder = os.path.join(BASE, f"life-path-{n1}-and-{n2}-compatibility")
        make_dir(folder)
        write(os.path.join(folder, "index.html"), compat_page(n1, n2, c, d1, d2))
        print(f"  ✦ /life-path-{n1}-and-{n2}-compatibility/")
        count += 1

# Update sitemap
print("\nUpdating sitemap.xml...")
urls = []
urls.append('<url><loc>https://luminanumbers.com/</loc><lastmod>2026-05-26</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>')
urls.append('<url><loc>https://luminanumbers.com/life-path-calculator/</loc><lastmod>2026-05-26</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>')

for n in DATA.keys():
    urls.append(f'<url><loc>https://luminanumbers.com/life-path-{n}-meaning/</loc><lastmod>2026-05-26</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>')

nums = list(DATA.keys())
for i in range(len(nums)):
    for j in range(i, len(nums)):
        n1, n2 = nums[i], nums[j]
        urls.append(f'<url><loc>https://luminanumbers.com/life-path-{n1}-and-{n2}-compatibility/</loc><lastmod>2026-05-26</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>')

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "\n".join(urls)
sitemap += "\n</urlset>"

write(os.path.join(BASE, "sitemap.xml"), sitemap)
print("  ✦ sitemap.xml updated")

print(f"\n✦ Done! Generated {count} pages total")
print(f"  - 12 meaning pages")
print(f"  - {count - 12} compatibility pages")
print(f"  - sitemap.xml updated with all URLs")
print(f"\nNext: GitHub Desktop → Commit → Push → Done!")
