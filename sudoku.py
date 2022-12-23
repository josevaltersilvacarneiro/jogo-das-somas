#!/usr/bin/env python

from game import Game

def fox() -> None:

     print('''
[0m[38;2;5;84;143m'[0m[38;2;6;85;144m'[0m[38;2;5;85;144m'[0m[38;2;6;86;145m'[0m[38;2;7;87;146m'[0m[38;2;7;86;146m'[0m[38;2;8;86;148m'[0m[38;2;8;87;149m'[0m[38;2;9;88;150m'[0m[38;2;9;89;150m'[0m[38;2;9;89;150m'[0m[38;2;10;90;151m'[0m[38;2;10;90;151m'[0m[38;2;11;91;152m'[0m[38;2;11;91;152m'[0m[38;2;11;91;152m'[0m[38;2;12;92;153m'[0m[38;2;13;93;154m,[0m[38;2;13;93;154m,[0m[38;2;14;94;155m,[0m[38;2;14;94;155m,[0m[38;2;16;96;156m,[0m[38;2;17;96;155m,[0m[38;2;18;97;156m,[0m[38;2;18;97;156m,[0m[38;2;18;97;156m,[0m[38;2;19;98;157m,[0m[38;2;20;99;158m,[0m[38;2;20;99;158m,[0m[38;2;20;99;158m,[0m[38;2;21;100;159m,[0m[38;2;21;100;159m,[0m[38;2;21;100;159m,[0m[38;2;23;102;161m,[0m[38;2;23;102;161m,[0m[38;2;25;102;162m,[0m[38;2;28;103;163m;[0m[38;2;29;103;161m;[0m[38;2;29;103;161m;[0m[38;2;30;105;162m;[0m[38;2;30;105;162m;[0m[38;2;30;105;162m;[0m[38;2;31;106;163m;[0m[38;2;32;107;164m;[0m[38;2;32;107;164m;[0m[38;2;32;107;164m;[0m[38;2;33;108;163m;[0m[38;2;35;108;163m;[0m[38;2;36;109;164m;[0m[38;2;36;109;164m;[0m[38;2;37;110;165m;[0m[38;2;38;110;166m;[0m[38;2;39;110;166m;[0m[38;2;39;110;166m;[0m
[0m[38;2;5;84;145m'[0m[38;2;5;85;145m'[0m[38;2;6;86;147m'[0m[38;2;7;87;148m'[0m[38;2;7;87;148m'[0m[38;2;7;88;149m'[0m[38;2;8;88;150m'[0m[38;2;9;89;150m'[0m[38;2;9;89;150m'[0m[38;2;9;90;151m'[0m[38;2;10;90;152m'[0m[38;2;11;91;152m'[0m[38;2;10;90;152m'[0m[38;2;11;91;153m'[0m[38;2;12;92;153m'[0m[38;2;12;92;153m'[0m[38;2;13;93;154m,[0m[38;2;13;93;155m,[0m[38;2;14;94;155m,[0m[38;2;14;94;156m,[0m[38;2;15;95;157m,[0m[38;2;16;96;158m,[0m[38;2;17;97;158m,[0m[38;2;17;97;158m,[0m[38;2;18;98;159m,[0m[38;2;18;98;158m,[0m[38;2;18;98;159m,[0m[38;2;19;98;159m,[0m[38;2;20;99;160m,[0m[38;2;20;99;160m,[0m[38;2;21;99;160m,[0m[38;2;21;100;161m,[0m[38;2;22;101;161m,[0m[38;2;23;102;161m,[0m[38;2;23;102;161m,[0m[38;2;24;103;162m,[0m[38;2;26;104;163m;[0m[38;2;27;105;164m;[0m[38;2;26;105;163m;[0m[38;2;27;105;164m;[0m[38;2;29;105;164m;[0m[38;2;30;105;164m;[0m[38;2;30;106;163m;[0m[38;2;31;107;164m;[0m[38;2;32;107;165m;[0m[38;2;33;107;165m;[0m[38;2;33;108;165m;[0m[38;2;33;108;165m;[0m[38;2;34;109;166m;[0m[38;2;34;109;165m;[0m[38;2;35;110;165m;[0m[38;2;36;111;166m;[0m[38;2;38;111;166m;[0m[38;2;38;111;166m;[0m
[0m[38;2;5;86;148m'[0m[38;2;7;87;150m'[0m[38;2;7;88;150m'[0m[38;2;7;88;151m'[0m[38;2;8;88;151m'[0m[38;2;8;89;152m'[0m[38;2;8;89;152m'[0m[38;2;9;89;153m'[0m[38;2;8;89;153m'[0m[38;2;10;91;155m'[0m[38;2;12;91;153m'[0m[38;2;9;91;155m'[0m[38;2;10;92;156m'[0m[38;2;10;92;156m'[0m[38;2;10;93;156m,[0m[38;2;11;94;157m,[0m[38;2;13;94;158m,[0m[38;2;14;95;159m,[0m[38;2;14;95;159m,[0m[38;2;15;96;159m,[0m[38;2;16;97;160m,[0m[38;2;16;97;160m,[0m[38;2;16;97;160m,[0m[38;2;17;98;161m,[0m[38;2;18;98;161m,[0m[38;2;18;99;161m,[0m[38;2;18;99;161m,[0m[38;2;19;100;162m,[0m[38;2;20;100;163m,[0m[38;2;20;100;163m,[0m[38;2;21;101;163m,[0m[38;2;21;101;163m,[0m[38;2;22;102;164m,[0m[38;2;23;103;164m,[0m[38;2;23;103;164m,[0m[38;2;24;104;164m;[0m[38;2;25;105;165m;[0m[38;2;25;105;165m;[0m[38;2;26;105;166m;[0m[38;2;27;105;166m;[0m[38;2;27;105;166m;[0m[38;2;27;106;166m;[0m[38;2;28;106;167m;[0m[38;2;29;106;164m;[0m[38;2;30;106;166m;[0m[38;2;30;108;167m;[0m[38;2;32;109;166m;[0m[38;2;33;109;166m;[0m[38;2;34;109;166m;[0m[38;2;35;110;167m;[0m[38;2;35;110;167m;[0m[38;2;36;111;167m;[0m[38;2;37;111;167m;[0m[38;2;39;113;169m;[0m
[0m[38;2;6;88;152m'[0m[38;2;6;88;152m'[0m[38;2;6;89;152m'[0m[38;2;6;90;154m'[0m[38;2;7;91;155m'[0m[38;2;7;91;155m'[0m[38;2;6;90;154m'[0m[38;2;7;91;155m'[0m[38;2;8;91;155m'[0m[38;2;43;114;169m:[0m[38;2;79;143;192ml[0m[38;2;44;119;178m:[0m[38;2;64;131;183mc[0m[38;2;36;111;170m;[0m[38;2;11;94;158m,[0m[38;2;11;95;160m,[0m[38;2;13;95;160m,[0m[38;2;13;97;161m,[0m[38;2;13;97;161m,[0m[38;2;13;97;161m,[0m[38;2;14;98;162m,[0m[38;2;15;98;162m,[0m[38;2;15;99;163m,[0m[38;2;15;99;163m,[0m[38;2;16;100;164m,[0m[38;2;16;100;164m,[0m[38;2;16;100;164m,[0m[38;2;18;100;164m,[0m[38;2;19;101;165m,[0m[38;2;20;101;165m,[0m[38;2;21;102;165m,[0m[38;2;21;102;165m,[0m[38;2;22;103;166m,[0m[38;2;22;103;166m,[0m[38;2;23;103;166m,[0m[38;2;24;105;167m;[0m[38;2;25;105;167m;[0m[38;2;25;106;167m;[0m[38;2;25;105;167m;[0m[38;2;26;105;167m;[0m[38;2;41;114;176m:[0m[38;2;69;134;186mc[0m[38;2;48;122;182m:[0m[38;2;60;131;186mc[0m[38;2;74;137;185ml[0m[38;2;30;108;168m;[0m[38;2;31;109;168m;[0m[38;2;31;110;168m;[0m[38;2;32;110;169m;[0m[38;2;33;111;170m;[0m[38;2;35;111;170m;[0m[38;2;35;110;168m;[0m[38;2;35;111;168m;[0m[38;2;37;113;170m;[0m
[0m[38;2;6;90;154m'[0m[38;2;6;90;155m'[0m[38;2;6;90;156m'[0m[38;2;7;90;156m'[0m[38;2;7;91;157m'[0m[38;2;8;92;158m'[0m[38;2;7;92;158m'[0m[38;2;6;92;158m'[0m[38;2;9;92;157m'[0m[38;2;83;142;189ml[0m[38;2;4;98;173m,[0m[38;2;1;98;175m,[0m[38;2;3;99;175m,[0m[38;2;43;119;182m:[0m[38;2;88;147;192mo[0m[38;2;28;106;166m;[0m[38;2;11;96;163m,[0m[38;2;13;96;163m,[0m[38;2;14;97;163m,[0m[38;2;14;98;164m,[0m[38;2;15;98;164m,[0m[38;2;15;99;165m,[0m[38;2;15;99;165m,[0m[38;2;16;99;164m,[0m[38;2;16;100;164m,[0m[38;2;17;100;165m,[0m[38;2;17;101;165m,[0m[38;2;17;101;165m,[0m[38;2;18;102;166m,[0m[38;2;19;102;167m,[0m[38;2;20;103;167m,[0m[38;2;20;103;167m,[0m[38;2;21;103;168m,[0m[38;2;21;104;168m,[0m[38;2;23;106;169m;[0m[38;2;23;105;169m;[0m[38;2;24;105;169m;[0m[38;2;24;106;168m;[0m[38;2;29;108;169m;[0m[38;2;89;147;191mo[0m[38;2;53;125;185mc[0m[38;2;3;98;173m,[0m[38;2;1;98;175m,[0m[38;2;2;97;174m,[0m[38;2;80;144;189ml[0m[38;2;30;108;170m;[0m[38;2;29;109;169m;[0m[38;2;30;110;170m;[0m[38;2;30;110;170m;[0m[38;2;32;111;170m;[0m[38;2;33;112;171m;[0m[38;2;32;112;170m;[0m[38;2;33;112;171m;[0m[38;2;34;113;170m;[0m
[0m[38;2;6;90;157m'[0m[38;2;5;91;158m'[0m[38;2;5;92;159m'[0m[38;2;6;92;159m'[0m[38;2;6;93;160m'[0m[38;2;6;93;160m'[0m[38;2;6;93;160m'[0m[38;2;7;93;160m'[0m[38;2;38;112;169m;[0m[38;2;34;114;180m;[0m[38;2;1;99;175m,[0m[38;2;1;99;176m,[0m[38;2;1;99;175m,[0m[38;2;2;99;175m,[0m[38;2;10;99;174m,[0m[38;2;112;162;201md[0m[38;2;63;129;183mc[0m[38;2;11;98;166m,[0m[38;2;11;99;164m,[0m[38;2;12;98;165m,[0m[38;2;13;100;167m,[0m[38;2;13;100;166m,[0m[38;2;14;100;167m,[0m[38;2;14;101;167m,[0m[38;2;14;101;167m,[0m[38;2;16;101;167m,[0m[38;2;17;101;168m,[0m[38;2;18;102;169m,[0m[38;2;18;102;169m,[0m[38;2;18;102;168m,[0m[38;2;19;103;169m,[0m[38;2;20;103;168m,[0m[38;2;21;105;169m;[0m[38;2;22;106;170m;[0m[38;2;22;106;170m;[0m[38;2;22;105;170m;[0m[38;2;21;105;170m;[0m[38;2;50;122;180m:[0m[38;2;122;170;204mx[0m[38;2;17;104;176m,[0m[38;2;2;98;174m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;99;175m,[0m[38;2;17;105;177m;[0m[38;2;60;130;182mc[0m[38;2;29;109;171m;[0m[38;2;30;110;172m;[0m[38;2;31;111;171m;[0m[38;2;31;111;171m;[0m[38;2;32;111;172m;[0m[38;2;32;111;172m;[0m[38;2;33;112;171m;[0m[38;2;34;113;173m;[0m
[0m[38;2;4;92;159m'[0m[38;2;4;92;159m'[0m[38;2;5;93;160m'[0m[38;2;5;93;161m'[0m[38;2;5;93;161m'[0m[38;2;6;93;162m'[0m[38;2;5;95;162m,[0m[38;2;7;94;162m,[0m[38;2;44;119;178m:[0m[38;2;2;98;175m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;2;99;176m,[0m[38;2;53;124;182m:[0m[38;2;68;137;191ml[0m[38;2;15;99;172m,[0m[38;2;176;204;223m0[0m[38;2;108;158;199md[0m[38;2;10;98;166m,[0m[38;2;11;99;168m,[0m[38;2;13;100;168m,[0m[38;2;13;100;167m,[0m[38;2;14;101;169m,[0m[38;2;14;101;168m,[0m[38;2;14;101;168m,[0m[38;2;15;102;169m,[0m[38;2;15;102;169m,[0m[38;2;16;103;169m,[0m[38;2;17;102;171m,[0m[38;2;20;103;168m,[0m[38;2;28;108;171m;[0m[38;2;18;103;171m,[0m[38;2;20;105;171m,[0m[38;2;20;105;172m;[0m[38;2;22;105;171m;[0m[38;2;18;103;171m,[0m[38;2;85;144;192ml[0m[38;2;196;217;231mK[0m[38;2;24;103;173m;[0m[38;2;57;129;187mc[0m[38;2;65;133;187mc[0m[38;2;4;99;174m,[0m[38;2;0;99;175m,[0m[38;2;0;100;176m,[0m[38;2;2;99;175m,[0m[38;2;48;122;184m:[0m[38;2;27;109;172m;[0m[38;2;28;110;174m;[0m[38;2;30;111;173m;[0m[38;2;30;111;173m;[0m[38;2;32;112;174m;[0m[38;2;32;112;174m;[0m[38;2;32;112;173m;[0m[38;2;32;112;173m;[0m
[0m[38;2;3;93;162m'[0m[38;2;3;94;162m'[0m[38;2;4;95;163m,[0m[38;2;4;95;163m,[0m[38;2;5;95;164m,[0m[38;2;4;95;163m,[0m[38;2;4;95;165m,[0m[38;2;7;94;165m,[0m[38;2;36;113;181m;[0m[38;2;1;99;175m,[0m[38;2;0;99;175m,[0m[38;2;0;99;176m,[0m[38;2;1;98;175m,[0m[38;2;5;97;173m,[0m[38;2;106;157;199md[0m[38;2;190;211;226mK[0m[38;2;176;201;220m0[0m[38;2;247;251;250mM[0m[38;2;101;157;198md[0m[38;2;6;99;173m,[0m[38;2;10;99;169m,[0m[38;2;11;101;169m,[0m[38;2;12;101;169m,[0m[38;2;13;101;170m,[0m[38;2;13;101;170m,[0m[38;2;22;107;172m;[0m[38;2;27;109;174m;[0m[38;2;39;117;178m:[0m[38;2;76;137;186ml[0m[38;2;107;158;198md[0m[38;2;71;135;182mc[0m[38;2;71;138;184ml[0m[38;2;23;108;171m;[0m[38;2;17;105;173m,[0m[38;2;9;100;172m,[0m[38;2;69;135;187mc[0m[38;2;245;249;248mW[0m[38;2;196;214;227mK[0m[38;2;188;209;226mK[0m[38;2;128;171;206mx[0m[38;2;9;100;174m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;0;99;176m,[0m[38;2;2;99;175m,[0m[38;2;35;119;184m:[0m[38;2;25;108;171m;[0m[38;2;28;110;175m;[0m[38;2;28;110;174m;[0m[38;2;29;111;174m;[0m[38;2;30;112;175m;[0m[38;2;30;112;175m;[0m[38;2;31;112;174m;[0m[38;2;32;112;174m;[0m
[0m[38;2;4;95;165m,[0m[38;2;3;94;164m'[0m[38;2;4;95;165m,[0m[38;2;4;95;165m,[0m[38;2;5;96;166m,[0m[38;2;5;97;166m,[0m[38;2;6;97;167m,[0m[38;2;5;97;167m,[0m[38;2;8;100;171m,[0m[38;2;1;99;176m,[0m[38;2;0;99;175m,[0m[38;2;3;98;174m,[0m[38;2;38;117;181m:[0m[38;2;98;153;197mo[0m[38;2;167;196;217mO[0m[38;2;224;233;238mN[0m[38;2;236;243;244mW[0m[38;2;241;246;246mW[0m[38;2;129;171;202mx[0m[38;2;3;98;174m,[0m[38;2;1;99;174m,[0m[38;2;3;100;174m,[0m[38;2;3;100;174m,[0m[38;2;3;100;174m,[0m[38;2;11;104;177m,[0m[38;2;10;102;176m,[0m[38;2;1;98;175m,[0m[38;2;1;98;174m,[0m[38;2;3;99;176m,[0m[38;2;23;109;176m;[0m[38;2;61;131;185mc[0m[38;2;40;118;178m:[0m[38;2;17;105;175m,[0m[38;2;2;98;173m,[0m[38;2;2;99;176m,[0m[38;2;100;153;195mo[0m[38;2;237;242;243mW[0m[38;2;239;245;246mW[0m[38;2;225;235;238mN[0m[38;2;179;205;222m0[0m[38;2;105;159;201md[0m[38;2;46;122;184m:[0m[38;2;4;98;174m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;17;106;175m;[0m[38;2;26;110;174m;[0m[38;2;27;111;175m;[0m[38;2;27;111;175m;[0m[38;2;27;111;175m;[0m[38;2;28;112;176m;[0m[38;2;28;112;176m;[0m[38;2;30;111;174m;[0m[38;2;31;112;175m;[0m
[0m[38;2;3;96;165m,[0m[38;2;3;96;165m,[0m[38;2;4;96;166m,[0m[38;2;4;96;166m,[0m[38;2;4;96;166m,[0m[38;2;4;96;166m,[0m[38;2;6;98;168m,[0m[38;2;6;99;168m,[0m[38;2;4;98;169m,[0m[38;2;0;99;174m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;1;99;174m,[0m[38;2;16;105;176m,[0m[38;2;45;119;181m:[0m[38;2;110;160;200md[0m[38;2;177;201;221m0[0m[38;2;135;176;207mx[0m[38;2;40;116;181m:[0m[38;2;3;99;175m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;1;100;175m,[0m[38;2;1;100;175m,[0m[38;2;0;100;175m,[0m[38;2;0;99;175m,[0m[38;2;0;99;175m,[0m[38;2;0;99;174m,[0m[38;2;2;98;176m,[0m[38;2;28;109;175m;[0m[38;2;124;169;206mx[0m[38;2;179;203;219m0[0m[38;2;123;168;203mx[0m[38;2;52;123;182m:[0m[38;2;21;109;177m;[0m[38;2;2;99;175m,[0m[38;2;1;99;177m,[0m[38;2;1;99;175m,[0m[38;2;1;98;175m,[0m[38;2;18;105;175m;[0m[38;2;25;110;175m;[0m[38;2;26;110;175m;[0m[38;2;27;111;176m;[0m[38;2;27;111;176m;[0m[38;2;27;111;175m;[0m[38;2;28;112;176m;[0m[38;2;28;112;176m;[0m[38;2;28;112;176m;[0m
[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;5;98;168m,[0m[38;2;6;99;169m,[0m[38;2;6;99;169m,[0m[38;2;6;97;168m,[0m[38;2;50;125;184m:[0m[38;2;4;98;173m,[0m[38;2;16;106;176m;[0m[38;2;4;98;175m,[0m[38;2;48;121;181m:[0m[38;2;122;168;202mx[0m[38;2;225;235;240mN[0m[38;2;217;229;235mX[0m[38;2;202;219;229mX[0m[38;2;185;210;228mK[0m[38;2;69;135;188mc[0m[38;2;1;97;174m,[0m[38;2;1;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;99;175m,[0m[38;2;2;98;175m,[0m[38;2;50;123;183m:[0m[38;2;175;202;224m0[0m[38;2;199;218;228mK[0m[38;2;217;229;236mN[0m[38;2;227;237;242mN[0m[38;2;145;181;211mk[0m[38;2;57;127;183mc[0m[38;2;6;98;174m,[0m[38;2;17;106;175m;[0m[38;2;2;98;172m,[0m[38;2;49;125;185m:[0m[38;2;25;110;175m;[0m[38;2;22;110;175m;[0m[38;2;24;110;177m;[0m[38;2;26;110;178m;[0m[38;2;27;110;178m;[0m[38;2;27;110;176m;[0m[38;2;27;111;175m;[0m[38;2;27;111;175m;[0m[38;2;28;112;176m;[0m
[0m[38;2;3;96;166m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;5;98;168m,[0m[38;2;6;99;169m,[0m[38;2;6;99;169m,[0m[38;2;5;98;168m,[0m[38;2;6;99;169m,[0m[38;2;6;98;168m,[0m[38;2;56;127;181mc[0m[38;2;164;198;222mO[0m[38;2;100;152;195mo[0m[38;2;152;188;213mO[0m[38;2;127;168;203mx[0m[38;2;183;206;221m0[0m[38;2;149;184;210mk[0m[38;2;139;181;212mk[0m[38;2;129;173;209mx[0m[38;2;26;110;178m;[0m[38;2;1;97;174m,[0m[38;2;0;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;99;176m,[0m[38;2;1;99;176m,[0m[38;2;1;99;176m,[0m[38;2;17;105;176m;[0m[38;2;117;166;205md[0m[38;2;142;182;213mk[0m[38;2;147;184;213mk[0m[38;2;180;205;220m0[0m[38;2;131;172;203mx[0m[38;2;151;187;215mO[0m[38;2;104;154;194mo[0m[38;2;154;189;216mO[0m[38;2;92;151;195mo[0m[38;2;21;108;175m;[0m[38;2;22;109;176m;[0m[38;2;23;110;177m;[0m[38;2;23;110;177m;[0m[38;2;24;110;177m;[0m[38;2;25;110;177m;[0m[38;2;27;110;178m;[0m[38;2;27;110;177m;[0m[38;2;27;111;177m;[0m
[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;5;98;168m,[0m[38;2;6;99;170m,[0m[38;2;6;98;171m,[0m[38;2;6;98;171m,[0m[38;2;5;98;169m,[0m[38;2;6;98;170m,[0m[38;2;5;99;168m,[0m[38;2;42;117;176m:[0m[38;2;106;160;203md[0m[38;2;108;160;200md[0m[38;2;137;181;213mk[0m[38;2;103;158;201md[0m[38;2;46;121;180m:[0m[38;2;3;98;173m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;0;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;1;100;175m,[0m[38;2;1;99;176m,[0m[38;2;2;99;175m,[0m[38;2;36;114;177m;[0m[38;2;96;152;196mo[0m[38;2;136;180;214mk[0m[38;2;115;164;205md[0m[38;2;97;153;198mo[0m[38;2;68;138;187ml[0m[38;2;21;107;175m;[0m[38;2;21;107;175m;[0m[38;2;21;108;175m;[0m[38;2;22;109;176m;[0m[38;2;22;109;176m;[0m[38;2;23;110;177m;[0m[38;2;23;110;177m;[0m[38;2;24;110;177m;[0m[38;2;25;110;178m;[0m[38;2;26;110;178m;[0m
[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;5;98;168m,[0m[38;2;5;98;169m,[0m[38;2;6;98;171m,[0m[38;2;6;98;171m,[0m[38;2;6;98;169m,[0m[38;2;5;98;168m,[0m[38;2;20;104;171m,[0m[38;2;130;174;204mx[0m[38;2;31;113;177m;[0m[38;2;1;99;175m,[0m[38;2;1;99;176m,[0m[38;2;1;99;176m,[0m[38;2;1;99;174m,[0m[38;2;9;103;177m,[0m[38;2;2;99;174m,[0m[38;2;1;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;175m,[0m[38;2;0;100;177m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;99;175m,[0m[38;2;2;98;175m,[0m[38;2;9;102;177m,[0m[38;2;2;98;175m,[0m[38;2;0;99;175m,[0m[38;2;1;99;175m,[0m[38;2;1;98;176m,[0m[38;2;18;106;176m;[0m[38;2;128;173;205mx[0m[38;2;50;125;180m:[0m[38;2;20;107;174m;[0m[38;2;20;108;175m;[0m[38;2;21;108;175m;[0m[38;2;22;109;176m;[0m[38;2;22;109;176m;[0m[38;2;22;109;176m;[0m[38;2;23;110;177m;[0m[38;2;23;110;177m;[0m[38;2;23;110;177m;[0m
[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;6;99;168m,[0m[38;2;5;98;170m,[0m[38;2;6;98;169m,[0m[38;2;5;98;168m,[0m[38;2;30;112;174m;[0m[38;2;79;137;184ml[0m[38;2;43;120;181m:[0m[38;2;1;97;173m,[0m[38;2;0;99;176m,[0m[38;2;0;100;175m,[0m[38;2;1;98;174m,[0m[38;2;11;101;176m,[0m[38;2;36;114;179m;[0m[38;2;47;120;181m:[0m[38;2;47;124;185m:[0m[38;2;8;100;174m,[0m[38;2;1;99;174m,[0m[38;2;0;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;1;99;175m,[0m[38;2;5;99;175m,[0m[38;2;43;121;182m:[0m[38;2;46;122;182m:[0m[38;2;37;114;177m;[0m[38;2;15;105;177m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;99;176m,[0m[38;2;1;99;175m,[0m[38;2;23;107;177m;[0m[38;2;90;147;191mo[0m[38;2;50;126;182m:[0m[38;2;19;106;175m;[0m[38;2;19;107;174m;[0m[38;2;20;107;174m;[0m[38;2;20;108;174m;[0m[38;2;21;108;175m;[0m[38;2;22;109;176m;[0m[38;2;22;109;176m;[0m[38;2;22;109;176m;[0m[38;2;23;110;177m;[0m
[0m[38;2;3;96;166m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;5;98;168m,[0m[38;2;5;98;169m,[0m[38;2;31;110;173m;[0m[38;2;104;155;194mo[0m[38;2;72;136;190ml[0m[38;2;7;99;174m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;99;175m,[0m[38;2;6;100;176m,[0m[38;2;65;133;187mc[0m[38;2;146;184;214mk[0m[38;2;145;183;211mk[0m[38;2;137;177;208mk[0m[38;2;79;140;190ml[0m[38;2;9;100;174m,[0m[38;2;1;98;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;1;99;175m,[0m[38;2;4;98;174m,[0m[38;2;71;135;188ml[0m[38;2;129;169;203mx[0m[38;2;145;182;212mk[0m[38;2;151;188;215mO[0m[38;2;78;141;190ml[0m[38;2;10;103;177m,[0m[38;2;0;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;99;176m,[0m[38;2;1;98;176m,[0m[38;2;2;96;173m,[0m[38;2;60;128;186mc[0m[38;2;100;153;194mo[0m[38;2;59;130;186mc[0m[38;2;18;106;175m;[0m[38;2;19;107;175m;[0m[38;2;19;107;175m;[0m[38;2;20;107;175m;[0m[38;2;20;107;175m;[0m[38;2;20;108;174m;[0m[38;2;21;108;175m;[0m[38;2;21;108;175m;[0m
[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;97;167m,[0m[38;2;4;96;166m,[0m[38;2;4;97;167m,[0m[38;2;5;97;166m,[0m[38;2;101;153;193mo[0m[38;2;192;211;224mK[0m[38;2;60;129;187mc[0m[38;2;2;99;174m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;99;175m,[0m[38;2;1;99;176m,[0m[38;2;1;99;175m,[0m[38;2;14;104;176m,[0m[38;2;76;142;194ml[0m[38;2;113;165;206md[0m[38;2;87;144;191ml[0m[38;2;94;149;195mo[0m[38;2;4;97;172m,[0m[38;2;1;99;175m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;2;98;175m,[0m[38;2;84;143;190ml[0m[38;2;81;140;190ml[0m[38;2;116;168;207mx[0m[38;2;84;147;196mo[0m[38;2;23;110;178m;[0m[38;2;1;98;175m,[0m[38;2;1;99;175m,[0m[38;2;0;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;175m,[0m[38;2;0;99;176m,[0m[38;2;1;98;174m,[0m[38;2;34;115;179m;[0m[38;2;181;207;224m0[0m[38;2;136;177;205mx[0m[38;2;17;105;172m,[0m[38;2;17;106;174m;[0m[38;2;18;106;175m;[0m[38;2;18;106;174m;[0m[38;2;19;107;174m;[0m[38;2;20;107;173m;[0m[38;2;20;107;174m;[0m[38;2;21;108;175m;[0m
[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;3;96;166m,[0m[38;2;4;96;166m,[0m[38;2;41;117;176m:[0m[38;2;213;228;237mX[0m[38;2;105;153;192mo[0m[38;2;62;131;185mc[0m[38;2;3;99;175m,[0m[38;2;1;99;176m,[0m[38;2;2;98;174m,[0m[38;2;33;115;180m;[0m[38;2;80;147;195ml[0m[38;2;92;152;199mo[0m[38;2;57;131;189mc[0m[38;2;16;106;176m,[0m[38;2;2;99;175m,[0m[38;2;1;98;174m,[0m[38;2;1;98;173m,[0m[38;2;66;137;188ml[0m[38;2;16;102;172m,[0m[38;2;1;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;2;96;171m,[0m[38;2;76;139;189ml[0m[38;2;2;98;177m,[0m[38;2;1;99;175m,[0m[38;2;1;99;175m,[0m[38;2;11;102;174m,[0m[38;2;52;128;187mc[0m[38;2;88;151;197mo[0m[38;2;86;150;198mo[0m[38;2;40;120;182m:[0m[38;2;3;99;174m,[0m[38;2;1;99;174m,[0m[38;2;1;99;176m,[0m[38;2;51;125;183m:[0m[38;2;86;141;188ml[0m[38;2;214;229;236mX[0m[38;2;81;142;189ml[0m[38;2;17;105;174m,[0m[38;2;15;106;173m,[0m[38;2;16;105;174m,[0m[38;2;17;105;174m;[0m[38;2;18;105;173m,[0m[38;2;19;106;173m;[0m[38;2;20;107;174m;[0m
[0m[38;2;2;95;165m'[0m[38;2;2;95;165m'[0m[38;2;2;95;165m'[0m[38;2;2;95;165m,[0m[38;2;3;96;166m,[0m[38;2;2;95;165m'[0m[38;2;5;94;165m,[0m[38;2;146;184;210mk[0m[38;2;140;178;207mk[0m[38;2;102;152;192mo[0m[38;2;54;127;185mc[0m[38;2;5;100;174m,[0m[38;2;9;99;173m,[0m[38;2;115;163;201md[0m[38;2;185;210;226mK[0m[38;2;199;217;226mK[0m[38;2;229;238;240mN[0m[38;2;251;252;250mM[0m[38;2;244;248;250mW[0m[38;2;195;215;230mK[0m[38;2;78;142;192ml[0m[38;2;2;97;173m,[0m[38;2;26;112;179m;[0m[38;2;4;97;172m,[0m[38;2;0;99;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;0;100;176m,[0m[38;2;2;98;173m,[0m[38;2;26;112;180m;[0m[38;2;3;98;175m,[0m[38;2;59;129;187mc[0m[38;2;183;209;224m0[0m[38;2;239;245;248mW[0m[38;2;251;252;250mM[0m[38;2;236;242;245mW[0m[38;2;202;218;227mK[0m[38;2;191;213;228mK[0m[38;2;131;174;207mx[0m[38;2;17;104;174m,[0m[38;2;5;100;175m,[0m[38;2;20;103;174m,[0m[38;2;124;171;204mx[0m[38;2;113;163;199md[0m[38;2;184;209;225mK[0m[38;2;15;101;169m,[0m[38;2;14;104;172m,[0m[38;2;16;103;171m,[0m[38;2;16;103;171m,[0m[38;2;17;104;171m,[0m[38;2;17;104;171m,[0m[38;2;17;104;171m,[0m
[0m[38;2;2;93;163m'[0m[38;2;2;93;163m'[0m[38;2;2;93;164m'[0m[38;2;2;94;164m'[0m[38;2;2;94;164m'[0m[38;2;2;94;164m'[0m[38;2;6;93;163m'[0m[38;2;56;125;179mc[0m[38;2;4;93;165m'[0m[38;2;110;160;200md[0m[38;2;50;120;177m:[0m[38;2;23;104;171m;[0m[38;2;38;114;177m:[0m[38;2;81;140;187ml[0m[38;2;87;146;191mo[0m[38;2;121;166;200mx[0m[38;2;180;206;223m0[0m[38;2;243;247;248mW[0m[38;2;253;253;252mM[0m[38;2;253;254;253mM[0m[38;2;240;246;248mW[0m[38;2;53;125;183mc[0m[38;2;43;120;179m:[0m[38;2;4;98;175m,[0m[38;2;1;98;174m,[0m[38;2;1;98;175m,[0m[38;2;1;98;174m,[0m[38;2;2;98;175m,[0m[38;2;2;99;175m,[0m[38;2;1;99;175m,[0m[38;2;2;98;174m,[0m[38;2;46;121;182m:[0m[38;2;32;109;177m;[0m[38;2;225;236;243mN[0m[38;2;253;254;253mM[0m[38;2;253;254;253mM[0m[38;2;247;249;248mW[0m[38;2;191;213;226mK[0m[38;2;128;172;204mx[0m[38;2;93;150;194mo[0m[38;2;82;143;189ml[0m[38;2;52;124;183m:[0m[38;2;21;107;173m;[0m[38;2;43;116;178m:[0m[38;2;124;167;199mx[0m[38;2;13;102;170m,[0m[38;2;54;127;182mc[0m[38;2;25;108;172m;[0m[38;2;14;102;169m,[0m[38;2;15;102;170m,[0m[38;2;15;102;169m,[0m[38;2;16;103;170m,[0m[38;2;16;103;170m,[0m[38;2;16;103;170m,[0m
[0m[38;2;1;92;162m'[0m[38;2;2;93;162m'[0m[38;2;2;93;163m'[0m[38;2;2;93;163m'[0m[38;2;3;94;163m'[0m[38;2;2;94;163m'[0m[38;2;2;93;163m'[0m[38;2;3;94;163m'[0m[38;2;3;93;163m'[0m[38;2;40;116;174m:[0m[38;2;15;98;165m,[0m[38;2;4;94;166m,[0m[38;2;3;95;164m,[0m[38;2;3;95;165m,[0m[38;2;3;95;165m'[0m[38;2;3;95;165m,[0m[38;2;5;95;163m,[0m[38;2;49;120;177m:[0m[38;2;147;183;213mk[0m[38;2;238;244;246mW[0m[38;2;252;253;251mM[0m[38;2;168;194;214mO[0m[38;2;146;183;211mk[0m[38;2;6;98;174m,[0m[38;2;33;114;179m;[0m[38;2;47;123;184m:[0m[38;2;54;126;185mc[0m[38;2;54;127;184mc[0m[38;2;46;123;183m:[0m[38;2;38;118;180m:[0m[38;2;4;96;172m,[0m[38;2;136;179;210mk[0m[38;2;152;182;207mk[0m[38;2;251;252;251mM[0m[38;2;246;249;249mW[0m[38;2;165;195;219mO[0m[38;2;63;131;183mc[0m[38;2;11;100;167m,[0m[38;2;10;100;167m,[0m[38;2;10;100;168m,[0m[38;2;11;101;169m,[0m[38;2;12;101;169m,[0m[38;2;11;100;169m,[0m[38;2;13;101;167m,[0m[38;2;53;124;178m:[0m[38;2;12;100;167m,[0m[38;2;13;100;167m,[0m[38;2;13;101;170m,[0m[38;2;14;101;169m,[0m[38;2;14;101;168m,[0m[38;2;15;102;169m,[0m[38;2;15;102;169m,[0m[38;2;15;102;169m,[0m[38;2;15;102;169m,[0m
[0m[38;2;1;90;158m'[0m[38;2;2;91;159m'[0m[38;2;3;93;160m'[0m[38;2;2;93;161m'[0m[38;2;2;93;160m'[0m[38;2;2;92;161m'[0m[38;2;2;93;162m'[0m[38;2;3;93;162m'[0m[38;2;2;93;162m'[0m[38;2;2;93;163m'[0m[38;2;3;93;161m'[0m[38;2;2;93;163m'[0m[38;2;3;94;164m'[0m[38;2;3;94;164m'[0m[38;2;4;95;165m,[0m[38;2;4;95;165m,[0m[38;2;3;94;164m'[0m[38;2;4;95;164m,[0m[38;2;4;95;165m,[0m[38;2;36;112;173m;[0m[38;2;165;196;219mO[0m[38;2;164;192;211mO[0m[38;2;247;251;249mM[0m[38;2;200;218;231mK[0m[38;2;126;173;209mx[0m[38;2;15;103;175m,[0m[38;2;2;99;174m,[0m[38;2;1;98;175m,[0m[38;2;9;98;174m,[0m[38;2;109;161;204md[0m[38;2;190;212;228mK[0m[38;2;248;250;251mM[0m[38;2;164;192;213mO[0m[38;2;183;209;227mK[0m[38;2;51;122;179m:[0m[38;2;8;98;167m,[0m[38;2;10;98;167m,[0m[38;2;10;99;167m,[0m[38;2;10;99;167m,[0m[38;2;10;99;167m,[0m[38;2;10;99;166m,[0m[38;2;10;99;167m,[0m[38;2;11;99;168m,[0m[38;2;11;99;167m,[0m[38;2;12;99;167m,[0m[38;2;12;99;166m,[0m[38;2;12;99;166m,[0m[38;2;13;100;167m,[0m[38;2;13;100;167m,[0m[38;2;14;100;167m,[0m[38;2;14;100;167m,[0m[38;2;13;100;167m,[0m[38;2;14;100;167m,[0m[38;2;14;100;167m,[0m
[0m[38;2;1;89;158m'[0m[38;2;2;89;158m'[0m[38;2;1;89;158m'[0m[38;2;1;90;158m'[0m[38;2;2;91;159m'[0m[38;2;3;92;160m'[0m[38;2;3;92;160m'[0m[38;2;3;92;160m'[0m[38;2;3;92;160m'[0m[38;2;2;92;160m'[0m[38;2;2;92;160m'[0m[38;2;2;92;161m'[0m[38;2;3;93;161m'[0m[38;2;2;93;161m'[0m[38;2;2;94;162m'[0m[38;2;3;95;162m'[0m[38;2;3;94;163m'[0m[38;2;3;94;164m'[0m[38;2;3;94;163m'[0m[38;2;3;93;163m'[0m[38;2;5;93;162m'[0m[38;2;72;134;182mc[0m[38;2;193;213;225mK[0m[38;2;242;246;247mW[0m[38;2;251;253;251mM[0m[38;2;217;232;239mN[0m[38;2;60;131;186mc[0m[38;2;39;117;182m:[0m[38;2;208;226;237mX[0m[38;2;252;252;252mM[0m[38;2;247;250;249mW[0m[38;2;205;222;229mX[0m[38;2;91;146;189mo[0m[38;2;11;96;166m,[0m[38;2;8;96;165m,[0m[38;2;8;97;165m,[0m[38;2;9;98;166m,[0m[38;2;9;98;166m,[0m[38;2;9;97;165m,[0m[38;2;10;97;164m,[0m[38;2;10;97;163m,[0m[38;2;10;97;164m,[0m[38;2;11;98;165m,[0m[38;2;11;98;165m,[0m[38;2;11;98;165m,[0m[38;2;11;98;165m,[0m[38;2;10;97;164m,[0m[38;2;11;98;165m,[0m[38;2;13;98;165m,[0m[38;2;14;98;166m,[0m[38;2;14;98;166m,[0m[38;2;14;98;165m,[0m[38;2;14;98;164m,[0m[38;2;14;98;163m,[0m
[0m[38;2;1;87;154m'[0m[38;2;1;88;155m'[0m[38;2;2;88;155m'[0m[38;2;2;88;155m'[0m[38;2;2;89;156m'[0m[38;2;2;90;156m'[0m[38;2;2;90;157m'[0m[38;2;2;90;157m'[0m[38;2;2;90;157m'[0m[38;2;3;90;158m'[0m[38;2;3;90;158m'[0m[38;2;3;91;159m'[0m[38;2;3;91;159m'[0m[38;2;3;91;159m'[0m[38;2;2;91;159m'[0m[38;2;3;92;160m'[0m[38;2;4;92;160m'[0m[38;2;4;92;160m'[0m[38;2;4;92;160m'[0m[38;2;3;92;160m'[0m[38;2;3;92;161m'[0m[38;2;6;91;159m'[0m[38;2;36;112;173m;[0m[38;2;116;163;199md[0m[38;2;152;188;215mO[0m[38;2;131;174;208mx[0m[38;2;116;167;207mx[0m[38;2;114;167;206md[0m[38;2;128;171;205mx[0m[38;2;151;186;213mk[0m[38;2;125;169;202mx[0m[38;2;46;120;176m:[0m[38;2;6;94;160m'[0m[38;2;7;94;161m,[0m[38;2;7;94;162m,[0m[38;2;7;94;162m,[0m[38;2;7;94;162m,[0m[38;2;7;94;162m,[0m[38;2;8;95;162m,[0m[38;2;9;96;163m,[0m[38;2;10;96;163m,[0m[38;2;10;96;163m,[0m[38;2;10;96;163m,[0m[38;2;10;96;163m,[0m[38;2;10;96;163m,[0m[38;2;10;95;163m,[0m[38;2;11;95;163m,[0m[38;2;12;96;162m,[0m[38;2;12;96;162m,[0m[38;2;12;95;162m,[0m[38;2;12;95;161m,[0m[38;2;13;96;161m,[0m[38;2;13;97;161m,[0m[38;2;12;96;160m,[0m
[0m[38;2;1;85;149m'[0m[38;2;1;85;151m'[0m[38;2;2;85;152m'[0m[38;2;2;85;152m'[0m[38;2;2;86;152m'[0m[38;2;3;87;153m'[0m[38;2;2;87;154m'[0m[38;2;1;88;154m'[0m[38;2;2;89;155m'[0m[38;2;2;89;155m'[0m[38;2;2;89;155m'[0m[38;2;3;89;155m'[0m[38;2;3;89;156m'[0m[38;2;3;89;156m'[0m[38;2;3;89;157m'[0m[38;2;3;89;157m'[0m[38;2;3;90;157m'[0m[38;2;3;90;158m'[0m[38;2;3;90;158m'[0m[38;2;3;91;158m'[0m[38;2;4;91;158m'[0m[38;2;4;91;158m'[0m[38;2;3;91;158m'[0m[38;2;4;90;158m'[0m[38;2;5;92;160m'[0m[38;2;5;92;160m'[0m[38;2;5;92;159m'[0m[38;2;5;91;159m'[0m[38;2;5;91;159m'[0m[38;2;6;92;161m'[0m[38;2;6;92;160m'[0m[38;2;6;92;159m'[0m[38;2;6;93;160m'[0m[38;2;6;93;159m'[0m[38;2;6;93;159m'[0m[38;2;6;92;159m'[0m[38;2;7;92;159m'[0m[38;2;8;92;160m'[0m[38;2;6;94;159m'[0m[38;2;7;93;159m'[0m[38;2;9;93;159m,[0m[38;2;10;93;159m,[0m[38;2;10;93;159m,[0m[38;2;10;93;158m,[0m[38;2;10;94;158m,[0m[38;2;10;94;158m,[0m[38;2;9;93;158m,[0m[38;2;10;94;158m,[0m[38;2;10;94;158m,[0m[38;2;10;93;157m,[0m[38;2;10;93;157m,[0m[38;2;10;94;157m,[0m[38;2;10;94;156m,[0m[38;2;10;93;156m,[0m
[0m[38;2;1;83;147m'[0m[38;2;1;84;147m'[0m[38;2;1;84;147m'[0m[38;2;0;84;148m'[0m[38;2;1;84;148m'[0m[38;2;1;85;149m'[0m[38;2;1;85;149m'[0m[38;2;1;85;149m'[0m[38;2;2;86;150m'[0m[38;2;3;87;151m'[0m[38;2;3;87;151m'[0m[38;2;4;88;151m'[0m[38;2;4;88;153m'[0m[38;2;4;88;153m'[0m[38;2;4;88;154m'[0m[38;2;4;87;155m'[0m[38;2;4;88;155m'[0m[38;2;4;88;155m'[0m[38;2;3;88;155m'[0m[38;2;4;89;156m'[0m[38;2;4;89;155m'[0m[38;2;4;89;154m'[0m[38;2;4;90;155m'[0m[38;2;4;89;155m'[0m[38;2;5;90;156m'[0m[38;2;5;90;155m'[0m[38;2;5;90;155m'[0m[38;2;4;90;155m'[0m[38;2;6;91;156m'[0m[38;2;7;91;157m'[0m[38;2;7;91;157m'[0m[38;2;7;91;157m'[0m[38;2;7;91;157m'[0m[38;2;7;91;157m'[0m[38;2;7;90;155m'[0m[38;2;7;91;155m'[0m[38;2;7;91;156m'[0m[38;2;7;90;156m'[0m[38;2;7;91;155m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;8;92;156m'[0m[38;2;9;92;156m'[0m[38;2;10;92;155m'[0m[38;2;9;92;155m'[0m[38;2;10;91;155m'[0m[38;2;11;92;155m'[0m[38;2;11;92;154m'[0m[38;2;11;91;153m'[0m[38;2;11;91;153m'[0m
[0m[38;2;1;82;145m'[0m[38;2;2;83;146m'[0m[38;2;2;83;146m'[0m[38;2;1;83;146m'[0m[38;2;1;83;146m'[0m[38;2;1;83;146m'[0m[38;2;2;84;147m'[0m[38;2;2;84;147m'[0m[38;2;1;84;147m'[0m[38;2;1;85;148m'[0m[38;2;2;86;150m'[0m[38;2;2;86;150m'[0m[38;2;2;86;150m'[0m[38;2;2;86;150m'[0m[38;2;2;86;150m'[0m[38;2;3;86;151m'[0m[38;2;2;86;151m'[0m[38;2;4;87;152m'[0m[38;2;4;87;153m'[0m[38;2;4;88;153m'[0m[38;2;4;88;152m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;5;89;153m'[0m[38;2;5;89;153m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;154m'[0m[38;2;6;90;153m'[0m[38;2;6;90;154m'[0m[38;2;7;90;154m'[0m[38;2;8;90;154m'[0m[38;2;8;90;153m'[0m[38;2;9;90;153m'[0m[38;2;9;90;153m'[0m[38;2;9;90;153m'[0m[38;2;9;90;153m'[0m[38;2;10;90;153m'[0m[38;2;10;90;152m'[0m[38;2;10;90;151m'[0m[38;2;11;91;152m'[0m
     ''')

def main() -> int:

    game = Game();

    while not game.quit:

        game.show();
        game.play();

    else:
        game.show();

    # Cute cute

    fox()

    return 0;

if __name__ == '__main__':
    exit(main());
