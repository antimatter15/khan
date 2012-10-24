At time of writing, a video is being processed by my `v2.py` script, it's only eight lines of code thanks to the beautifully terse nature of python and SimpleCV. And since it's clearly not operating at the breakneck speed of one frame per second, I don't have time to write this README, meaning that I'm writing this README. But since I haven't actually put a description of this project out in writing before, I think it's important to start off with an introduction.

It's been over a year since I first wrote code for this project. It really dates back to late April 2011. Certainly it wouldn't have been possible to write the processor in eight painless lines of python back then, when SimpleCV was considerably in more of an infancy. I'm pretty sure that puts the pre-production stage of this project in about the range of a usual Hollywood movie production. However, that's really quite unusual for me because I don't tend to wait to get started on projects often. Or at least, I usually publish something in a somewhat workable state before abandoning it for a year.

However, the fact is that this project has been dormant for more than an entire year. Not necessarily because I lost interest in it, but because it always seemed like a problem harder than I had been comfortable tackling at any given moment. There's a sort of paradox that afflicts me, and probably other students (documented by that awesome Calvin and Hobbes comic) where at some point, you find a problem hard enough that it gets perpetually delayed until, of course, the deadline comes up and you end up rushing to finish it in some manner that only poses a vague semblance to the intent. 

The basic premise is somewhat simple: videos aren't usually the answer. That's not to say video isn't awesome, because it certainly is. YouTube, Vimeo and others provide an absolutely brilliant service, but those platforms are used for things that they aren't particularly well suited for. Video hosting services have to be so absurdly general because there is this need to encompass every single use case in a content-neutral manner. 

One particular example is with music, which often gets thrown on YouTube in the absence of somewhere else to stick it. A video hosting site is pretty inadequate, in part because it tries to optimize the wrong kinds of interactions. Having a big player window is useless, having an auto-hiding progress slider and having mediocre playback, playlist and looping interfaces are signs that a certain interface is being used for the wrong kind of content. Contrast this to a service like SoundCloud which is entirely devoted to the interacting with music. 

The purpose of this project is somewhat similar. It's to experiment with creating an interface for video lectures that goes above, in terms of interactivity and in terms of usability (perhaps even accessibility), what a simple video can do. 

So yeah, that's the concept that I came up with a year ago. I'm pretty sure it sounds like a pretty nice premise, but really at this point the old adage of "execution is everything" starts to come into play. How exactly is this going to be better than video? 

One thing that's constantly annoyed me about anything video-related is the little progress slider tracker thing. Even for a short video, I always end up on the wrong spot. YouTube has the little coverflow-esque window which gives little snapshots to help, and Apple has their drag down to do precision adjustment, but in the end the experience is far from optimal. This is especially unsuitable because moreso in lectures than perhaps in any other type of content, you really want to be able to step back and go over some little thing again. Having to risk cognitive derailment just to go over something you don't quite get can't possibly be good. 


At this point, the processing is almost done, I'd say about 90%, so I don't have much time to say anything else. I really want this to work out, but of course, it might not. Whatever happens, It's going to be something.

### Captain's Log Tuesday October 23, 2012

Ahoy! No, I actually can't speak like a pirate, so I think it would probably be better if I didn't even bother trying. It's not even talk like a pirate day, and I am so far away from seafaring lingo, that I should probably stop now before I incriminate myself any more in front of the grand oceanic tribunal.

Today, I basically rewrite `v2.py` which is the SimpleCV based script which actually tries to vectorize the contents of a Khan Academy video. At this point, 