from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# List of items to vote on
items = [
            "Deletee (intro)", "Safehouse", "Ebay", "Shadowface Spellbound", "Everlasting Flames", 
            "Freeze", "Upgrade Enabled", "Unreal", "Dragonfly", "Into Dust", "Who Goes There", 
            "So What", "Lovenote", "Missing Person", "Romeo Xd Out", "Sick", "Rip", "Bloodveil / Stillborn",
            "Sugar", "Wrist Cry", "Skin", "7-Eleven", "Butterfly", "MJ", "Psycho", "50SACINMYSOCIDGAF",
            "Still in Search of Sunshine", "Painkillers", "1 million", "Brokeboy", "Area 51", "2X", "Winter",
            "Destroy me", "Gotham City", "No Life Left", "First Crush", "Numb/Beverly Hills", "Cinderella",
            "Wickr Man", "Suffocation", "Dumpster Baby", "Scarecrows", "Botox Lips", "Stalker", "Relight Moments",
            "Red Velvet", "Lordship", "Trash Star", "Knightsbridge", "All I Want", "Backstr€€t Boys", "Apple",
            "Under Your Spell", "Vanilla Sky", "D-925", "30th Floor", "Gatekeeper", "Waterfall", "Cherry Bracelets",
            "Victim", "Best Buy", "Western Union", "1D", "The Void", "Golden Boy", "Acid Rain", "Westfield",
            "You Lose", "Fake News", "Undergone", "Steve Jobs", "Mirror (Hymn) (Intro)", "Obedient", "Wonderland",
            "For You", "Merry-Go-Round", "Hex", "Rain3ow Star (Love is All)", "Nike Just Do It", 
            "Every Moment Special", "That Thing You Do", "DNA Rain", "Decay", "Open Symbols (Play) Be in Your Mind",
            "College Boy", "Lovestory", "Puppet Master", "Imaginary", "I'm Goofy", "Opium Dreams", "Sesame Street",
            "Wings in Motion", "I.E.E.", "Don't Worry", "Smile", "Keys to the City", "Plastic Surgery",
            "Hero of My Story 3style3", "It Suxx", "100s", "Doorman", "Mean Girls", "Trial", "Innocent of All Things",
            "Sentence", "Reality Surf", "I Chose to Be This Way", "Noblest Strive", "SmartWater", "It Girl", 
            "OKK", "Oh Well", "Mallwhore Freeestyle", "Valerie", "Ben Nice 2 Me", "Finder", "Frosty the Snowman",
            "Extasia", "Inside Out", "Only One", "Close", "Swan Lake", "Jaws", "Intro", "Cartier'god Icedancer (Intermission)",
            "Rainbow", "Side by Side", "Sun", "Topman", "God", "Waster", "Drama", "Special Place", "You", 
            "Dg Jeans", "Into One", "Feel Like", "Grace", "Linkdin", "Gates", "For Nothing", "The Fool Intro", 
            "Anything", "Let's Ride", "The Silent Boy Cries (Ripsquadd Outro)", "Hotel Breakfast", "I Think..", 
            "Thee 9 ls Up", "Desiree", "I Want It That Way", "Bby", "Inspiration Comes", "Egobaby Trendy", "Search True", 
            "Wett (Water2)", "SHINIE", "Amygdala", "The Flag Is Raised", "5 Star Crest (4 Vattenrum)", "White Meadow", 
            "Faust", "Yeses (Red Cross)", "Desire Is a Trap Chaos Follows", "Girls Just Want to Have Fun", 
            "Heaven Sings", "DRAIN STORY", "Understatement", "Its OK to Not Be OK I Am Slowly but", "Nothingg", 
            "Blue Crush Angel", "Disaster Prelude", "Hahah", "Drain Story", "Velociraptor", "Dresden ER", 
            "She's Always Dancing", "Uriel Outro Real Spring", "Every Summer", "Yxguden", "Requiem", "Obsessed with Death", 
            "Coda", "Ghosts", "Golden God", "Still", "Sold Out", "Hanging from the Bridge", "Enemy", "Things Happen", 
            "TL;DR", "Paranoia Intro", "Wodrainer", "Yung Sherman", "Flatline", "One Second", "Sad Meal", "Fun Fact", 
            "Only God Is Made Perfect", "Don't Wanna Hang Out", "I Don't Like People (Whitearmor Interlude)", 
            "I Don't Like People", "End of the Road Boyz", "D.O.A", "Don't Do Drugz", "Lows Partlyy", "So Cold Interlude", 
            "Message to Myself Terrible Excellence", "Red Cross", "Lucky Luke", "River Flows in You", "King Nothingg", 
            "Bad 4 Business", "Otherside", "Normal", "Flexing and Finessing", "PM2", "False", "Can't End on a Loss (Outro)", 
            "Cold Visions (Outro 2)", "Rewind featuring bladee"]

# Results file path
RESULTS_FILE = "results.txt"

# Ensure results file exists and initialize with 0 counts
if not os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "w") as f:
        for item in items:
            f.write(f"{item}: 0\n")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_items = request.form.getlist("votes")
        if selected_items:
            # Update vote counts in the results file
            update_vote_counts(selected_items)
            return redirect(url_for("thanks"))
        else:
            return redirect(url_for("index"))

    # Shuffle items for fairness
    import random
    shuffled_items = items[:]
    random.shuffle(shuffled_items)
    return render_template("index.html", items=shuffled_items)

@app.route("/thanks")
def thanks():
    return "Thank you for voting! Your vote has been recorded."

def update_vote_counts(selected_items):
    """Update the vote counts in the results file."""
    # Read the current counts
    counts = {}
    with open(RESULTS_FILE, "r") as f:
        for line in f:
            item, count = line.rsplit(": ", 1)
            counts[item] = int(count.strip())

    # Increment the counts for selected items
    for item in selected_items:
        if item in counts:
            counts[item] += 1

    # Write the updated counts back to the file
    with open(RESULTS_FILE, "w") as f:
        for item, count in counts.items():
            f.write(f"{item}: {count}\n")

if __name__ == "__main__":
    app.run(debug=True)