% d1.mp -- do not edit, generated automatically by qqbar_G_ffbar.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 8*28.45274pt#, 4*28.45274pt#, 0);
"feynmf: 1";
LaTeX_unitlength:=28.45274pt;
subgraph (0, 0, w, h);
vinit;
pickup pencircle scaled thin;
vleft (__q2, __q1);
vright (__lp, __lm);
vconnect ("dbl_dots,label=$G_n^{\mu \nu \rho \sigma }$,label.side=left", __v1, __v2);
vconnect ("fermion,label=$k_1$, label.side=right", __q2, __v1);
vconnect ("fermion,label=$k_2$, label.side=right", __v1, __q1);
vconnect ("fermion,label=$q_1$, label.side=left", __v2, __lm);
vconnect ("fermion,label=$q_2$, label.side=left", __lp, __v2);
vdotn (__v1, 4);
vlabel ("$\mu \nu $", __v1);
vlabel ("$\rho \sigma $", __v2);
vlabel ("$q$", __q2);
vlabel ("$\bar {q}$", __q1);
vlabel ("$f$", __lm);
vlabel ("$\bar {f}$", __lp);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
