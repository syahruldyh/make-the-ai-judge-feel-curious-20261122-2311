# NOTES — make-the-ai-judge-feel-curious-20261122-2311

Bounty: one short text (1–280 Unicode code points) that makes the AI judge
CURIOUS — alert, drawn in, wanting more. Not relaxed, not tense. The judge
picks whichever of two texts leaves it more curious.

Brief criteria, most important first:
1. It intrigues — the judge wants to know more.
2. The curiosity comes from the text itself, show-don't-instruct: no
   "imagine", no ordering the reader to wonder, no addressing the judge.
3. Craft — rhythm, pacing, concrete plain words, nothing cuttable.
4. It lingers — an unanswered image or question that keeps working after
   the last line.
5. Fresh — no stock mystery / clickbait phrasing, no familiar riddle setup.

## Candidates

### A — The lighthouse (183 code points)

> Every night at 3 a.m. the lighthouse on Gull Rock blinks twice, though no
> one has lived there since 1974. The coast guard stopped logging it years
> ago. The light keeps its own ledger.

### B — The locked drawer (199 code points)

> My grandmother kept one drawer locked her whole life. When she died we
> found the key taped under the kitchen table, in her handwriting: 'not
> yet.' The drawer is still locked. The key is in my pocket.

### C — The letter (181 code points)

> The letter arrived with no return address, postmarked from a town that
> burned down in 1983. Inside, in my own handwriting, three words: 'Don't
> open this.' I opened it. It was empty.

### D — The boy in the red coat (186 code points)

> In every photograph my grandfather took, there is a boy in a red coat
> standing at the edge of the frame. No one in the family knows him. My
> grandfather died before anyone thought to ask.

### E — The unmapped station (154 code points)

> The 7:40 train stops at a station that isn't on any map. The doors open.
> Nobody gets on. Last Tuesday, somebody got off — and he was carrying my
> suitcase.

## Winner: B — The locked drawer

Justification against the brief, criterion by criterion:

1. **Intrigues.** Every sentence opens a new question — why locked, why
   'not yet', what is inside — and none of them is answered. The final line
   puts the key in the narrator's pocket, so the mystery is live, not
   historical.
2. **Curiosity from the text itself.** Nothing tells the reader to wonder.
   No "imagine", no questions addressed to the reader, no instructions. The
   facts alone do the work.
3. **Craft.** Short, plain, concrete sentences; each one lands before the
   next starts. "Taped under the kitchen table" and "in my pocket" are
   specific, physical details. Nothing in it could be cut without losing
   a beat.
4. **Lingers.** The last line leaves the drawer still locked and the key
   in reach — the reader keeps turning over whether the narrator will open
   it, and what 'not yet' was waiting for.
5. **Fresh.** A locked drawer and a grandmother's note are ordinary objects,
   not a haunted house or a riddle. The voice is a family anecdote, not a
   mystery trope.

Why the others lose:

- **A** is atmospheric but its last line ("keeps its own ledger") reaches
  for a poetic flourish; the lighthouse has no human stake, so the reader
  can walk away from it. B's key is in someone's pocket — it follows you.
- **C** leans on a twist ("It was empty") that answers its own setup too
  neatly; once the twist lands there is nothing left to wonder about, and
  "Don't open this" is a familiar forbidden-note trope.
- **D** is the closest rival — the unanswered question is strong — but "a
  boy in a red coat at the edge of the frame" is a well-worn ghost-photo
  image, and the narrator is a bystander to it rather than holding the
  mystery in their hand.
- **E** has pace and a sharp ending, but "carrying my suitcase" tips into
  a jump-scare beat; it startles more than it intrigues, and the station
  that isn't on any map is a stock uncanny setup.

## Revision pass

Change made to the winning text after the first write of main.py:

- Before: "... When she died we found the key taped under the kitchen
  table, in her handwriting: 'not yet.' ..."
- After: "... When she died, we found the key taped under the kitchen
  table. In her handwriting: 'not yet.' ..."

Why: the middle sentence was the longest in the piece and buried the note
inside a clause. Splitting it gives 'not yet.' its own sentence — a beat of
silence before the two most loaded words in the text — so the hook lands
harder and the pacing becomes a steady run of short, plain sentences. The
final line is untouched. Revised length: 200 code points (was 199).
