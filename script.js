const items = [
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
    "Cold Visions (Outro 2)", "Rewind featuring bladee"];
// Shuffle items for fairness
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Populate items dynamically
const itemsList = document.getElementById('itemsList');
shuffleArray(items).forEach(item => {
    const div = document.createElement('div');
    div.classList.add('item');
    div.innerHTML = `<label><input type="checkbox" name="votes" value="${item}"> ${item}</label>`;
    itemsList.appendChild(div);
});

// Submit votes
function submitVotes() {
    const selectedItems = Array.from(document.querySelectorAll('input[name="votes"]:checked')).map(input => input.value);
    if (selectedItems.length > 0) {
        fetch('https://script.google.com/macros/s/AKfycbx3_vT0AH37hb5HoEk6IJO8Lyl-ZUGF6h2X46hZx03rRvpjMIQMfqEKkwyB_2r83Veq/exec', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ votes: selectedItems }),
        })
        .then(response => response.json())
        .then(data => {
            alert("Votes submitted successfully!");
            console.log(data);
        })
        .catch(error => {
            alert("Failed to submit votes.");
            console.error(error);
        });
    } else {
        alert("Please select at least one item!");
    }
}