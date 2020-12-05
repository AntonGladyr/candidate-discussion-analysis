# Measuring perspectives on election legitimacy

## How to calculate top ten words per topic
Don't forget your `pip install -r requirements.txt`, and then try running:


`< data/tfidf-test-tweets-01.csv python3 scripts/tfidf.py`

Which should provide the output:

```

==================
nan
admin 0.015558007385094906
scientists 0.015558007385094906
man 0.015558007385094906
refund 0.015558007385094906
donated 0.015558007385094906
challenge 0.015558007385094906
jake 0.015558007385094906
tapper 0.015558007385094906
blunt 0.015558007385094906
reminder 0.015558007385094906

==================
Vote Turnout
florida 0.10466295877245664
latino 0.10466295877245664
community 0.10466295877245664
swing 0.10466295877245664
it’s 0.10466295877245664
complicated. 0.10466295877245664
did 0.07315626874700457
trump? 0.07315626874700457
why 0.05472603656026982
the 0.010142888696100444

==================
Elections
recount 0.018235890388020426
county 0.01580443833628437
votes 0.013372986284548314
milwaukee 0.013372986284548314
biden 0.012077868681199993
election 0.010643292556088391
fraud 0.008497560255723867
wisconsin 0.007294356155208171
vote 0.00509853615343432
by 0.00509853615343432

==================
Transition
biden 0.017880784222662417
transition 0.01709840415589638
become 0.011398936103930921
right 0.011398936103930921
office 0.011398936103930921
biden's 0.008940392111331208
no 0.007967514417990595
already 0.007967514417990595
with 0.0068628433718806465
state 0.006804139098075409

==================
Beliefs
tank 0.02616573969311416
economy 0.02616573969311416
vengeance? 0.02616573969311416
have 0.02616573969311416
done 0.02616573969311416
thomas 0.02616573969311416
frank: 0.02616573969311416
evicted, 0.02616573969311416
future 0.02616573969311416
built 0.02616573969311416

==================
Media
eric 0.026774245267372626
latest 0.026774245267372626
spread 0.026774245267372626
disinformation 0.026774245267372626
backfires 0.026774245267372626
like 0.026774245267372626
all 0.026774245267372626
rest 0.026774245267372626
caught 0.026774245267372626
sharing 0.026774245267372626

==================
Trump
#diaperdon 0.012076495242975766
thanksgiving 0.012076495242975766
talk 0.01125481057646224
donald 0.01052423780005189
at 0.009611441243435194
twitter 0.00844110793234668
ever 0.00844110793234668
an 0.008419390240041512
reporter 0.008419390240041512
event 0.00805099682865051

==================
Trump Admin
administration 0.016855619260563105
killing 0.013815510557964275
protections 0.012875503299472802
bird 0.009656627474604601
moves 0.009656627474604601
ahead 0.009210340371976183
gutting 0.009210340371976183
birds 0.009210340371976183
pardon 0.006437751649736401
court 0.006437751649736401

==================
Political Attitudes
supporters 0.07195578415606393
boycott 0.050294934763565634
races 0.050294934763565634
senate 0.037624150135185504
calling 0.03597789207803197
desperate 0.03597789207803197
midwesterners 0.03597789207803197
struggle, 0.03597789207803197
key 0.025147467381782817
call 0.025147467381782817

==================
Biden Admin
biden 0.02736301828013491
protect 0.011213888439906068
plan 0.011213888439906068
we 0.011213888439906068
and 0.010412394680388126
black 0.007475925626604046
cindy 0.007475925626604046
mccain 0.007475925626604046
ambassador 0.007475925626604046
uk 0.007475925626604046
```
