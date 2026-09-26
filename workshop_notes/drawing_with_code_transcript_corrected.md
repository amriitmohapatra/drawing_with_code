# Drawing with Code — Workshop Transcript (corrected)

Source: Otter.ai recording "Drawing with Code Workshop Overview" (2026-09-26, 44 min 49 s).
Speakers: **Kapi** (Speaker 1, presenter), **Participant** (Speaker 2, a PhD student in a quantitative field), Speaker 3 (brief, unclear).

## How to read this version

- Speech-to-text errors are corrected (names, artworks, tool names, technical terms). Filler and false starts are trimmed lightly; the meaning and order are unchanged.
- `[?]` marks a correction I'm fairly but not fully sure of. `[unclear: "…"]` keeps the original Otter text where I couldn't recover the words.
- **App-specific labels (tab names, preset names, slider names) could not be checked against the app**, because the cloud environment blocks `field-work-drawing.web.app`. They're marked `[verify]`.
- Where the speaker's own statement looks factually off (as opposed to a transcription error), I've left it as spoken and added a footnote.

---

**[0:00:02] Kapi:** The network name and password are on the screen right now. I'll show them again when we actually start the activity, in case you don't catch it now or haven't had time to connect.

Thank you, everybody, for showing up on this fine sunny Saturday afternoon here at the [unclear: "Agweb Aliwon"] Art Centre. My name is Kapi, and my collaborator Joe is sitting back there. Welcome to Drawing with Code, which is part of Fieldwork [?], which is taking over the [unclear: "joint"] building over the next five months.

I'm going to very briefly say hi and talk about us, in case there are a lot of new faces here. [unclear: "doing companies"] is made up of Joe and myself, and we are an art collective. We do a lot of curation and creation of works. We are both creative technologists by training, and we came from design and VR backgrounds — [unclear: "Analyzing drugs to be architecture"; possibly "I studied architecture"] — and then did media installations and video work for a while. Then we moved more into education: we're both currently teaching at [unclear: "the South College of the Arts"], and I also teach at [unclear: "Medium"], which is where I graduated from as well.

So that's a tiny bit about us. If you want to know more, you can follow us on socials, or come and talk to us later in real life.

Before we get started, I thought we'd do a very quick — not really a lecture, but a brief framework of what we're trying to do here: why you've got this beautifully done floral and fruit set-up, but also what this [unclear: "graph"] is doing. Before I ask you some questions, a quick show of hands: how many of you are here from a predominantly art or creative background? Quite a few. And everyone else, are you more from a tech background?

**[0:02:29] Participant:** I'm actually a PhD student, but my work is more in a quant field.

**[0:02:33] Kapi:** Wow, yeah.

**[0:02:35] Participant:** But I still have to come up with graphs that need to be presented in a certain way, so that they're not too complex for others to understand. So I get the importance of expression.

**[0:02:47] Kapi:** OK, yeah. I always like to do this in my classes as well — start with some meta, thought-provoking questions so we can ease into the framework of what's going on. I'd like to start with two questions today: **What does it mean to draw computationally?** And more importantly, **does computational art require a computer?**

Let's start with the first one. Does anyone want to take a stab at it — what does it mean to draw computationally? Anybody? … OK — using code or programming to draw. Yeah.

**[0:03:44] Participant:** Sometimes when I'm scrolling on Twitter, I see posts with videos where they use different mathematical equations to show different patterns.

**[0:03:54] Kapi:** Yeah.

**[0:03:55] Participant:** That's one way to do it.

**[0:03:56] Kapi:** Yeah, that's definitely one way of drawing computationally — through mathematical expression. I like to joke with my graphic design students that the "graph" in graphic design comes from the maths: actually graphing, creating forms. A lot of that is done mathematically in a computer, and harnessing that capability can help us find joy, and maybe creative expression, in the harder sciences.

For me, drawing computationally means approaching drawing as a computational practice. What that means and how I define it, I'll try to explain in a couple of slides.

Then the second question: does computational art require a computer? Everyone's silently shaking their heads. The consensus in the room seems to be that it doesn't, and I think that's an accurate statement: computational art does not require a computer. There are many ways to take a computational approach to drawing, creative expression and art-making that don't need a physical computing device to do the computation.

So I'll start by very briefly showing a history of people who have tackled both of these questions, and the kinds of work they've made.

The first one is **Sol LeWitt**. Those of you from the arts will probably be very familiar with him. LeWitt is famous for his series of instructional drawings. Here I have *Wall Drawing #122*, but he made many, many wall drawings as part of this series. The work isn't really what you see visually; it's a binder of instructions for how to make the work. I don't have the exact instructions for this one with me right now, but they specify the type of ink, the colours you use and the kinds of shapes you're allowed to make.

So each manifestation of the wall drawings — *Wall Drawing #260*, or #122 here, or #118 — looks similar, but they're never the same. The result is determined by the people who actually carry out the instructions. All LeWitt does is put the instructions in a literal binder. When a museum buys the work, it's essentially acquiring the binder of instructions, and then it needs the manpower to physically make the work. Each time these walls are staged they look slightly different, because people remember some instructions slightly differently, or there's a new vision, or the size of the space is different. And here you can see the wall drawing actually wraps around three walls, so if you want to interpret it that way, you can spread it across multiple walls.

The key thing is that the computational part of LeWitt's practice is that he's writing instructions — and that's how we work with computers: we give them instructions and get them to compute through different steps, which sometimes result in visuals or graphics.

Another legend and pioneer in this space is **Vera Molnár**, who took things one step further.¹ With LeWitt, a physical person interprets and executes the instructions. Molnár worked with something called a **pen plotter**. If you don't know what that is, it's like a 3D printer that only moves in two directions and uses a pen — that's the easiest way to describe it. So she's working one step beyond LeWitt: she writes the instructions and turns them into code that moves a physical pen plotter around, and the pen produces drawings. As a creative you also have more autonomy here, because you can change the type of pen, the viscosity of the ink, or replace the pen with a brush altogether, and get different outcomes. So there are a lot of ways to experiment with the computational process without feeling removed from it.

In the 80s we had a massive invention that changed everything: personal computing, and specifically the age of desktop publishing. I think the first true game-changer was the **Macintosh**, released in 1984, and more importantly **Bill Atkinson's** app **MacPaint**, which launched with it. For a lot of us — at least for me — my first memories of making graphics on a computer were with Microsoft Paint, because I didn't have a [unclear: "Windows machine"; possibly "Mac"] yet. But Microsoft Paint can trace its lineage directly to MacPaint.

MacPaint was completely monochrome — just black and white — and it was marketed with a really beautiful **ukiyo-e**-inspired picture made entirely in the software. And when the Mac was marketed as a personal computer, the famous "hello" on screen was also drawn in MacPaint. It was used to express that the machine was so human-like you could get nice handwritten strokes in an app. This was presumably done with a mouse; I can't find a real story about how it was made. Apple has since reused it — it came back in the last five years or so, as a way to market their history.

So now we see a confluence: where is the line between the human-made outcome and where the technology converges with the human in the loop? If you think about how **pen plotters** were about telling the computer how to draw, MacPaint gives us a way to draw directly through the computer itself, and it reframes how we move through the tool — from working a pen or pencil that moves with your hand, to [unclear: "which then moves across"].

Now fast-forward many decades. The next example is **Zach Lieberman** and his project ***Land Lines***, which I highly encourage you to Google and play with yourself. *Land Lines* is a really interesting project that uses satellite imagery from Google [Earth] maps,² and it tries to figure out the dominant stroke in each section of a map tile. So you see the movement of a river, an open road or a dirt track, and these come together under your mouse as you scribble. Instead of showing your scribbles, it finds the closest-matching map tile for the movement of your cursor, which creates a beautiful collage of satellite snapshots that come together to illustrate [unclear: "the mindset"] drawing.

This shifts the idea of what drawing or mark-making is, and how a computer can push the way we think about illustrative processes we usually take for granted when we're just working with a piece of paper and some medium to apply marks with.

So just to catch up: LeWitt's instructions led to drawings. Then Molnár took those instructions and turned them into algorithms, and the algorithms were physicalised into drawings with a pen plotter. With MacPaint we increased that abstraction further, with gesture-based tools translated into drawings on screen. And now, with *Land Lines*, we're turning those gestures into a real-time data visualisation — evolving a little more into poetics. What does it mean to draw a line, when all these lines come from all corners of the earth? [unclear: "And my father said represents people, yeah, yeah, yeah."]

Then there are people who push this even further. I have two examples. The first is **Matt DesLauriers**, and this is from a series called ***Meridian***. *Meridian* was published as a physical book; the first edition sold out and he published it again. He's really interested in how far you can take a pencil line and what the [unclear: "law"] is. He started creating this for the [unclear: "video market"; possibly "NFT market"], and he started turning a line into texture, and then bringing those textures together into

**[0:13:52] Speaker 3:** [appears to be Kapi continuing, mis-attributed] … sort of really working compositions that evoke a

**[0:13:54] Kapi:** sense of movement, or maybe stratification, or terrain. So layering together tiny shapes can become patterns, and you can create new sets of rules that eventually express themselves as a composition. In this way you're no longer thinking of the line as just a line. You're asking: how do I draw this object, and can I present it through a series of very small elements that together suggest motion, form or light? It's back to [unclear: "Pasco 101"; possibly "Drawing 101"] ideas — but this set of illustrations is all computer-generated. Matt DesLauriers wrote a series of programs that produce these outcomes, selected thousands of them and put them together in the book, also called *Meridian*. It's a beautifully printed volume, and I highly suggest you look it up if you're interested in how far this idea can be pushed.

On the other side of things we have **Tyler Hobbs** and his series ***Fidenza***. Joe and I were really lucky to show at the ArtScience Museum [?] alongside Tyler Hobbs a couple of years ago. His series brings us squarely into the contemporary, by thinking about the systems and elements available now that can power these works. *Fidenza* is a series of NFTs. I know NFTs are like slot machines, whatever. But the one really interesting thing about the blockchain and NFTs is that each token has a completely unique **hash**, or identity. Tyler Hobbs uses that unique identity as the **seed** that goes back into his program and expresses itself.

So *Fidenza* is kind of the [unclear: "logical version of mandatory"; possibly "logical extension of Meridian"]: you build these systems and tools that interact and work together to generate the form, but then you let the code take the wheel to some extent, letting each unique hash decide for itself. That gives an immutable version of the work that only exists because the rules of the code met that hash in a specific way. So instead of coding an entire picture from scratch, you can **code the conditions from which many pictures, or a system of outcomes, may emerge.**

That's something to think about later when you're exploring: what are the variable parameters [?], and what are the constant parameters [?]? Do I want to work with very strict rules — limiting myself to a specific number of lines, being very strict about how I space them, using a specific visual language and grammar for how I construct my work? These are more computational ways of approaching it.

The last person on my list is a Singaporean South Asian artist, [unclear: "Aniti"], who has been working on a series called [unclear: "Anatomy of a Boulder"; probably *Anatomy of a Kolam*]. Joe and I first worked with [her] for an exhibition we did called *Sorry for the Technical Difficulties*, which was about artists working with technology in ways it wasn't intended or designed for. In this example, she was very interested in exploring the mathematical and algorithmic nature of **kolams**. For those who aren't familiar, kolams are South Asian decorations placed at the thresholds of houses, usually made from rice flour. They follow a very specific system for how complex forms emerge. She was interested in dissecting these analytical principles and turning them back into a visualised, machine-assisted drawing system. She used a [unclear: "hand model"; probably "plotter"] that, instead of drawing with ink, draws directly on the floor with rice [flour/paste], the way a human would traditionally. She then explored slightly more contemporary extensions of the system, drawing with a [unclear: "white marker that really wanted maxim glass"], and the marker uses a custom ink made out of [unclear: rice?] as well.

So there's a huge breadth in how you can take a computational approach to drawing or mark-making, and producing these things doesn't need to be a one-sided, [unclear: "wings all"; possibly "winner-takes-all"] kind of competition. You don't have to reject technology and work only by hand, and inversely, you don't have to be purely tech-maxxing and only working on a computer. There can be very productive collaborations between the two, bringing out the best of both — which is what we're going to try to do today.

Thank you for listening to my little [unclear: "DF"; possibly "TED"] session. If you're interested in the kind of work Joe and I do, especially with Fieldwork, you can find us on socials here. But most importantly, follow us at [unclear: "Joy Company"] on Instagram to stay updated on more programmes we have from [unclear: "the rest here"] all the way to Singapore. I'll leave this up for a bit in case you want to take photos, and then we'll go into Drawing with Code proper.

### The app

All right, let's start to draw. This is the first time we're running Drawing with Code, and we thought getting you all straight into code would be too overwhelming — it's really intense. So we built a custom tool that lives at the URL at the top: **field-work-drawing.web.app**. For those of you familiar with Procreate, I've tried to mimic it so it doesn't look too foreign. But it is, for all intents and purposes, an app that gets you to think computationally and [unclear: "do my live robot and stuff"].

I'll give everybody some time to (a) connect to the Wi-Fi if you need to, and (b) get to the URL. Then I'll share my screen and talk you through the app before we start the programme properly. [Off-mic exchange about sharing the Wi-Fi password.]

OK, there we go. I'm on my iPad now, but you can do this on a tablet or a computer, whatever. [unclear: "Close your phone."] When you go to the page, you should see a very simple UI like this.

**Canvas.** You'll see this panel on the right-hand side, which we designed specifically for this session. There are some simple canvas settings. Because social media is everything these days, they're all very Instagram-friendly: **square**, **4:5** and **16:9** — all the defaults you need. You can also set the **paper colour**; by default it's a nice off-white, cream-looking paper. And there's a **grid** to help with composition.

**Tools.** Now the tools. There are a few you can use: **Draw**, **Paint**, **Boids** [verify] — I'll explain each — and **Erase**, which is self-explanatory.

**Draw.** With Draw, there's a little preview of the stroke you'll make. On a computer there's no pressure sensitivity, but on an iPad with an Apple Pencil that supports pressure — I'll just hover — you can see the app recognises that I have pressure sensitivity, so my stroke looks a bit more [unclear: "sexy"; possibly "expressive"]. When you hover you'll see a little dot showing where your brush will be, and then I can make a stroke. It behaves just like Procreate, and it's smooth.

**Size** makes your brush larger or smaller. Tap **Ink** and you can use your system's default colour picker to choose colours however you're comfortable. I usually leave it on the sliders so I can mix my colours any way I want. I'm going to choose this [unclear: "laminary"] colour. Unfortunately the projector isn't great, so what you see there is a bit more saturated. You can also play with **opacity**. If you're working with a stylus, adjusting the controls will require your finger, because the stylus gets priority on the canvas [?]. And if you don't want pressure sensitivity even though you have a stylus, just turn it off with this **pressure toggle** [verify]. There's also a **reset** button to put everything back to the way it was. [unclear: "Represent my purple."]

**System.** Next there's a section called **System** [verify], and right now everything's at 100% **strength**. There's a set of presets towards the bottom. Right now I have [unclear: "health"; verify — the default preset], which is the default. I can switch it to **Breathing**, **Restless**, **Wandering**, **Nervous** [verify all] and so on, and you'll notice each changes how the brushstrokes behave. Each preset is a set of computational algorithms that defines how your brushstrokes behave, and keep behaving, on screen.

To give it a slightly artsy vibe, I've kept the frame rate at 15 frames per second, so it looks a bit stop-motion. Fortunately [unclear: "we don't like the look of 50 frames per second"] — sorry — but it's also for performance: in case someone shows up with an iPad from ten years ago, it should still run OK. It's about accessibility — making this as accessible as possible for everybody.

If you want more control, tap **Custom** [verify] to reveal more options. There's [unclear: "rig"; possibly **Rate**/**Speed**, verify], which changes how quickly things animate. You can play with **Drift** and **Jitter** [verify], and **Displacement** [unclear: "displays"; verify], which is how far the line wanders after you draw it — so your marks don't have to feel fixed in place. There's a little switch that says **jump instead of wander** [verify]: instead of wandering smoothly, the line jumps around.

So if I draw something really gestural here — something like that — once I've finished the stroke, it behaves the way I've set it up. And each stroke can have different behaviours: I can come in and keep drawing with different settings, and each of my lines behaves slightly differently. These are very basic ways of mark-making, made computational by having them affected by these systems behind the scenes. Instead of exposing you to lines and lines of code, we've simplified the computational systems into a set of sliders that interact with one another, which together create either chaotic gestures or very smooth, fluid ones, depending on how you set them up.

**Paint.** I'm going to swap my colour to something else and go to the next tab, **Paint**. I really like the Paint tab because it involves computational aesthetics a bit more. Instead of painting things in as solid fills or blobs, the system turns them into nice grids of shapes, which you can apply as [unclear: "vanity"; possibly "loosely"] or as structured as you want. You can switch between different shapes that form the clusters, and you control the **area** — how big a region you paint. Oops, this area's really huge — now I can paint over a really large part. I can also control the **weight** — how thick or thin the lines appear — and the **size** of the shapes in my [unclear: "system block"].

So you have a lot of control over these computational systems behind the scenes. In programming we call them **loops**: if you're a coder, these are essentially nested `for` loops repeating shapes in the vertical and horizontal directions, **clipped** to the gestures you make — which is one of the basic things we learn in programming. You can of course change the ink colour to anything you want and see how the layers interact and what kind of blending possibilities you can create.

You'll see that the [unclear: "system training"; possibly "System panel"] still shows the **Strength** slider. Strength universally reins everything in, or lets it run free. So once you're done drawing, you can dial how wild the system is by adjusting strength. So that's Paint.

I'm going to clear my canvas so we have more room. You clear the canvas with the **trash bin** at the bottom right of the toolbar.

**Boids.** Now I'm moving on to **Boids** [transcribed as "boys"/"voids"]. In computing, boids are an algorithm someone came up with³ that mimics the natural world — specifically **flocking** behaviour: how swarms of bees, hornets or birds fly together. They all have slightly different characteristics, but … you know what, let me actually describe this properly. I have a drawing tool, so I should take this opportunity. Give me one second.

OK, there we go. You can describe boids simply: it's a computational system that thinks about different agents ("guys") in a scene, and they follow three principles. The first is **cohesion**: how near they stay to each other, [unclear: "how steady they hold here to the blue"]. Then there's **alignment** — let me use another colour — if all of them are heading in a specific direction, alignment is how well they steer in the same direction. And there's one more … the last one is slipping my mind [**separation**⁴], but it's also one of the factors that affects how these particles steer on screen and move around.

I've implemented a few different boids systems here, which you select from these presets, and they change how the boids move together. Again, instead of painting blocks, you can just draw a stroke and be very textural about it, and the system will exist within the gestures you make. You can change the **speed** of how fast they move, how wildly they move around, the **variety** of their sizes, how **dense** you want the field, and how **big or small** they are. Then you paint them into an area and they show up.

In this version of the app you have two shapes: a **circle** and a little pointy **triangle**. You can also set the **direction** they'll predominantly try to move in before you make the stroke. So if you want them always moving upwards, set that, bring the group over here, and you can see a bunch of these spiky boids moving upwards.

Again, you're working computationally — messing with these systems — within the boundaries of a gestural, artistic way of working. So this is basically Procreate-style tooling, and you have full freedom over how you work with it.

Every tool is affected by the **eraser**. If I erase some of my boids' area, they realise they can't move there, and move into the remaining area, where they carry on. The total number of boids you've made won't change; only the area they're active in changes. So that's a way to create a field of boids and shape its appearance later. You can use it for shading, to suggest motion, and you can mix it with all the other computational tools in the app. And again you can use the **Strength** slider in case you get tired of them moving around and want to calm them down.

So that's a quick rundown of the tools at your disposal. There's a huge variety of possible outcomes for thinking computationally while expressing yourself creatively: think about how each of these shapes and tools relates to how you layer colour or structure in the scene. Perhaps some shapes suit some of the flora in front of you, and some don't. Or you can break the rules — you could pick an entirely [unclear: "bar square"] and that could be right as well. We have a lot of drawing time, and a really gorgeous set-up that Joe has arranged [unclear: "all kinds of regular buildings"], so I highly encourage you to move around the room. [unclear: "We will do more of one particular like new point."] You can always switch it up. We also have power strips everywhere, so if your laptop or iPad runs low, you can charge.

**Interface notes.** This side panel can only be dismissed on touch devices; on a laptop it's always there because you have enough space to see everything [?⁵]. You can zoom in and out with **Cmd +/Cmd −** (or **Ctrl +/Ctrl −** on Windows), hit **Cmd 0/Ctrl 0** to go back to 100%, or tap between the two magnifier icons to get back to 100%.

There's also **undo and redo**, up to **100 steps**. It keeps your last 100 steps in memory as long as you don't refresh the page — so I can go all the way back to when I started, including clearing the screen. That's handy if you want to return to something. And if you want to dismiss the side panel on desktop, click the **eye** icon here and it'll hide.

**Export.** Last but not least, you can export your work. Let me go back to something a bit prettier. Hit the little **share arrow** just above the trash can and you'll see the share dialog, with two ways to export. You can export a **still**: I made **PNG** the default so you get as much quality out of the image as possible, [unclear: "because the concrete will be fried"; possibly "because JPEG compression will fry it"]. Or you can record a **video** of up to **15 seconds** of whatever's happening, including continuing to draw while the app records. Let me demonstrate. If I hit **Video**, there's a little red recording dot showing the 15 seconds of recording time. I can keep drawing, and all of that counts towards the recording. Now my recording's done, and you should see my pen strokes show up — there you go. These are the live gestures I made while the app recorded. Hit **Save MP4** and choose the save-video option, whether you're on iOS or a desktop browser, and it saves normally.

We'd love it if you'd share any pieces [?] you make today with us — there's a form at the end, and you can submit as many as you like. The form also asks for your Instagram handle, or whatever social handles you have, if you want us to tag you. If you put N/A, we won't tag you or post your work. It's up to you.

OK, thank you for listening a little longer. We now have the rest of the evening to keep using the tool and exploring the set-up in front of you. Please feel free to move from your seat if you want a new angle, or if you need us to adjust the lighting, we can figure that out too. Does anyone have any questions, or issues you're facing with the tool?

**[0:40:05] Speaker 3:** [unclear: "Every morning, fine on the computer."; probably "Everything's working fine on the computer."]

**[0:40:08] Kapi:** OK, great to hear. We're going to put some tunes on — some chill vibes [?] — and we'll walk around and help you get set up. Thank you, everyone, let's get drawing. We also have soft drinks by the pillar behind, and they're chilled, so feel free to grab one while you draw. Just be careful not to spill on the power strips.

**[0:41:06] Unknown speaker(s):** [Inaudible side conversation.]

---

## Notes

1. The speaker refers to Vera Molnár as "he"; Molnár (1924–2023) was a woman. The pronoun is corrected here to "she".
2. The recording says "Google Street Map, Street View, and satellite view". *Land Lines* (Zach Lieberman with Google Creative Lab / Data Arts Team, 2016) is built on Google Earth satellite imagery, not Street View.
3. The boids model is Craig Reynolds' (1986/87).
4. The third boids rule the speaker couldn't recall is **separation** (steer to avoid crowding neighbours). Otter's summary also infers this.
5. As transcribed, it's ambiguous whether the panel is dismissible only on touch devices or always visible on desktop. Later the speaker hides it on desktop with the eye icon, so the intended meaning may be "auto-collapses on touch devices; on desktop it stays open unless you hide it."

## Errors in Otter's own summary

- URL is given as `fieldwork-drawing.web.app`; the correct address is **`field-work-drawing.web.app`**.
- "Matt Delorean" should be **Matt DesLauriers**; "Aniti" is uncertain (see transcript).
- "display wander" should be **displacement** [verify]; "Voids Module" should be **Boids** [verify].

## Still to verify against the live app

Tab names (Draw / Paint / Boids / Erase), the System panel name, the default preset name (heard as "health"), the preset list (Breathing, Restless, Wandering, Nervous), the Custom sliders (heard as "rig", drift, jitter, "displays"), the jump/wander toggle wording, the pressure toggle label, the Paint sliders (area, weight, size), the Boids sliders (speed, variety, density, size, direction) and the export labels (Still/PNG, Video, Save MP4).
