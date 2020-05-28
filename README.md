# Thoth
A small program that turn a simple mark up system into a tex file and a PDF. Meant to allow fast notekeeping in printable format.

# Features
- Multiple document modes
- Output on both source tex file and PDF
- Customizable tex templates for every mode
- Custom Highlighting option for vim  & vscode

# Document Modes
- Lists (Deafult mode) usable for fast notekeeping
- CheatSheet 

# Default mode
## Code 
!default

## Special characthers
\# Section

\## Subsection

\### Subsubsection


\- Non enumerated list

\* Enumerated list

\_ Start/finish italic

\__ Start/finish bold


\| new column on a table

\- first lines separator in table

# Code estrcuture

- Decoder Module
- Output Module
- Auxiliary functions module

## Decoder Module

Takes previous line, next line and current lines. Outputs a number with the type of line.

### Line numbers accoring to type of line

#### Standard mode
Number | Type
-------|-------
0 | Normal text
1 | New Section
2 | New Subsection
3 | New SubSubsection
4 | New Paragrpah
5 | New Subparagraph

#### List Mode
Number | Type
-------|-------
110 | New non-enumerated list
120 | New item non-enumerated list
13X | Finish non-enumerated list
14X | Start and finish non-enumerated list
150 | New enumerated list
160 | New item enumerated list
17X | Finish enumerated list
18X | Start and finish enumerated list

#### Table Mode
Number | Type
-------|-------
21 | New table
22 | New line in table
23 | Finish table
