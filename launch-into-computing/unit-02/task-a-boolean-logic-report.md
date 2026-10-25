---
layout: default
---

# Task A: Boolean Logic in Modern Computing Systems

Boolean logic is a mathematical system that represents information through two values: true and false, commonly expressed as 1 and 0. Operators such as AND, OR and NOT allow computers to evaluate conditions and make decisions. I consider Boolean logic fundamental to modern computing because it connects decision-making in software with the physical operations performed by digital hardware.

One application of Boolean logic is information retrieval. In the Boolean retrieval model, search terms can be combined using AND, OR and NOT. For example, `EV charging AND cybersecurity` searches for documents related to both subjects, while NOT can exclude unwanted results. Manning, Raghavan and Schütze (2008) explain that documents in this model either satisfy the specified conditions or do not. This provides precise filtering but cannot independently determine how relevant a document is or fully understand context and user intention. Modern search engines therefore supplement Boolean filtering with ranking algorithms and natural language processing.

A more specialised real-world application can be found in electric vehicle charging systems. The conditions required to start a charging session can be represented as:

`Start = A ∧ V ∧ C ∧ ¬F`

Here, `A` represents successful authorisation, `V` means that the vehicle is connected, `C` indicates that the connector is available and `F` represents a critical fault. Charging can begin only when the user is authorised, the vehicle is connected, the connector is available and no critical fault exists. These conditions can be implemented through `if` statements in programming. At the hardware level, control decisions are supported by digital circuits composed of logic gates. Shannon (1938) demonstrated that Boolean algebra could be used to analyse and design switching circuits, establishing an important foundation for digital circuit design.

A second practical application is cybersecurity access control. An access decision may require a correct password AND successful multi-factor authentication AND an appropriate user role, while the account must NOT be blocked. Sandhu et al. (1996) explain that role-based access control associates permissions with roles and assigns users to appropriate roles. The system can consequently accept or reject an access request by evaluating several logical conditions.

In my work with EV charging systems, I observe that Boolean conditions enable chargers to make fast and consistent decisions. However, their accuracy depends on the quality of their inputs. A temporary PLC or network communication failure may cause one condition to appear false, preventing a valid charging session. An automated system may also interpret a communication problem as a hardware failure, leading to an inaccurate diagnosis or an unnecessary work order. Therefore, although Boolean logic provides an efficient foundation for modern computing, complex operational situations require contextual analysis and human oversight.

## References

Manning, C.D., Raghavan, P. and Schütze, H. (2008) *Introduction to Information Retrieval*. Cambridge: Cambridge University Press. Available at: https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html (Accessed: 7 August 2026).

Sandhu, R.S., Coyne, E.J., Feinstein, H.L. and Youman, C.E. (1996) ‘Role-based access control models’, *Computer*, 29(2), pp. 38–47. Available at: https://doi.org/10.1109/2.485845.

Shannon, C.E. (1938) ‘A symbolic analysis of relay and switching circuits’, *Transactions of the American Institute of Electrical Engineers*, 57(12), pp. 713–723. Available at: https://doi.org/10.1109/T-AIEE.1938.5057767.