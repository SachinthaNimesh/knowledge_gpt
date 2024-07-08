



Ethernaut Level 5 Walkthrough: Token - Metana

















































































 












Skip links* [Skip to primary navigation](#primary-nav)
* [Skip to content](#lqd-site-content)



 





 


 




Call us +1 415 416 0800 


















 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 








* [Solidity BootcampHot 🔥](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [Bootcamps](#) 








###### Web3

 






### Web3 Solidity Bootcamp



Most Popular 🔥
The most advanced Solidity curriculum on the internet











### Full Stack Web3 Beginner Bootcamp



New ✨ | Beginner 👨‍💻
Starting off with web development and seamlessly integrating web3 development











### Web3 Rust Bootcamp



Become an expert Solana blockchain developer with one course!














###### Coding + Career Growth

 




 








### Software Engineering Bootcamp



Become a Software Engineer - Balance everyday life commitments & launch your coding career in as little as 16 weeks











### Metana's JobCamp™️



Learn to make a lasting first impressions, network effectively & search for jobs with confidence.















 ![](https://metana.io/wp-content/uploads/2023/10/Screenshot-2023-10-25-at-7.51.33 PM-300x61.png) 




 Rated
the Best

 





 Ranked as the industry's premier Web3 bootcamp with a stellar 4.8/5 star rating on Course Report.

 




[Read more reviews here](/reviews/)












[Still Unsure?](https://formless.ai/c/6bPi6ASGJ4ge)
* [Resources](#)
	+ [Reviews](https://metana.io/reviews/)
	+ [Metana’s Job Guarantee](https://metana.io/job-guarantee/)
	+ [Tuition](https://metana.io/tuition/)
	+ [Events](https://metana.io/events/)
* [Blog](https://metana.io/blog/)

 





[Apply now](https://metana.typeform.com/general)






















 







 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 









Metana Bootcamps
----------------

 






* [Solidity BootcampHot 🔥](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [Full Stack Web3 Bootcamp](https://metana.io/web3-beginner-bootcamp/)
* [Rust Bootcamp](https://metana.io/web3-rust-bootcamp-solana-blockchain/)
* [Cybersecurity Bootcamp](https://metana.io/cybersecurity-bootcamp/)
* [AI & Machine Learning Bootcamp](https://metana.io/ai-machine-learning-bootcamp/)
* [Data Analytics Bootcamp](https://metana.io/data-analytics-bootcamp/)
* [Data Science Bootcamp](https://metana.io/data-science-bootcamp/)
* [Full Stack Bootcamp](https://metana.io/full-stack-software-engineer-bootcamp/)
* [Jobcamp](https://metana.io/jobcamp/)

 














Menu Items
----------

 






* [Blog](https://metana.io/blog/)
* [Metana’s Job Guarantee](https://metana.io/job-guarantee/)
* [Refer a Friend](https://metana.io/refer/)
* [Tuition](https://metana.io/tuition/)
* [Withdrawal and Refund Policy](https://metana.io/withdrawal-and-refund-policy/)

 









 








 [[email protected]](/cdn-cgi/l/email-protection)

 




 

[Facebook](https://www.facebook.com/metanahq) 


[Twitter](https://twitter.com/metanahq) 


[Linkedin](https://www.linkedin.com/school/metana/) 


























 [![Metana](https://metana.io/wp-content/uploads/2022/07/Metana-Logo.png)](https://metana.io/) 




[Apply now](https://metana.typeform.com/general)
























 
#### Table of Contents





 







Ethernaut Level 5 Walkthrough: Token
====================================

 



 * [Shiran Sukumar](https://metana.io/blog/author/shiran-sukumar/)
* [May 3, 2024](https://metana.io/blog/2024/05/03/)
* [Ethernaut Walkthrough](https://metana.io/blog/category/ethernaut-walkthrough/)














Hello Everyone! My name is Shiran Sukumar, I am a student at Metana. I wanted to share with you all a **walkthrough on how to approach and solve an Ethernaut challenge.** 


Ethernaut is a fantastic learning resource for Solidity and smart contract security. In **Ethernaut Level 5**, the **Token challenge**, we’re introduced to a deceptively simple token contract. Our mission? Exploit a vulnerability to acquire more than the 20 tokens we’ve been initially allocated.


Understanding the Vulnerability
-------------------------------


The Token contract *seems* straightforward:



```
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract Token {

    mapping(address => uint256) balances;

    uint256 public totalSupply;

    constructor(uint256 _initialSupply) public {

        balances[msg.sender] = totalSupply = _initialSupply;

    }

    function transfer(address _to, uint256 _value) public returns (bool) {

        require(balances[msg.sender] - _value >= 0);

        balances[msg.sender] -= _value;

        balances[_to] += _value;

        return true;

    }

    function balanceOf(address _owner) public view returns (uint256 balance) {

        return balances[_owner];

    }

}
```

As we walk through this code let’s make note of several key lines that will help us establish a vulnerability. 


1. We check the solidity version: 0.6.0
2. The `transfer` function allows us to move tokens around
3. We can check our balance using the `balanceOf` function.


In Solidity version 0.6.0  there are no automatic under/over flow checks and this specific contract has not used any safeguards (like SafeMath) against such attack. The critical flaw lies in the `transfer`  function. Notice how it only checks if the sender has sufficient balance `(balances[msg.sender] - _value >= 0)` before performing the transfer. This creates a potential for an integer underflow. What is an integer underflow? 


The Underflow Exploit
---------------------


1. Our player account starts with 20 tokens.
2. Imagine we try to transfer 21 tokens. Mathematically, our balance should become negative.
3. However, unsigned integers in Solidity cannot store negative values. If a subtraction results in a negative number, it wraps around to a huge positive value! (Think of a buffer to visual why this happens)


The Attack
----------


Cool, so now you get the approach. How do we actually execute this exploit? This guide assumes you are already familiar with Ethernaut challenges. Otherwise you will need to learn how to set up a wallet, get test ether, and connect to Ethernaut. 


1. **Connect to Ethernaut:** using your wallet (MetaMask, Rainbow, etc.) , connect to the Ethernaut Level 5 instance and select Token (challenge 05)


![ethernaut level 5walkthroughtoken](https://metana.io/wp-content/uploads/2024/04/1-1024x707.png)
2. **Get the Contract Instance:** Use the provided interface to obtain a reference to the vulnerable Token contract.


![get the contract instance](https://metana.io/wp-content/uploads/2024/04/2-1024x461.png)
3. **Check your initial balance**:  Call balanceOf()  function with your address, you can verify you have 20 tokens (you’ll see an object with words containing the value 20)


![check your initial balance](https://metana.io/wp-content/uploads/2024/04/image-4.png)
4. **Call the** `transfer` **function:**  Call `transfer` with a receiver address and a value exceeding your current balance (e.g., transfer 21 tokens to a random address).


* Construct the function call


![construct the function call](https://metana.io/wp-content/uploads/2024/04/Screenshot-2024-04-26-at-8.35.07 AM-1-1024x57.png)
* Verify your request and sign your transaction.


![Verify your request and sign your transaction.](https://metana.io/wp-content/uploads/2024/04/4b.png)
* Wait for the transaction to complete. You can take the tx Hash and look at it on [Etherscan](https://sepolia.etherscan.io/).


![Wait for the transaction to complete. You can take the tx Hash and look at it on Etherscan. ](https://metana.io/wp-content/uploads/2024/04/image-3.png)
5. **Massive Balance:** Check your balance. You’ll have a massively inflated token amount due to the underflow!


![massive balance](https://metana.io/wp-content/uploads/2024/04/6.png)
6. **Submit your Instance:** Click that Subit button on the interface and…..Celebrate and look at all those rainbows! You just completed Etherenaut Level 5!


![submit your instance](https://metana.io/wp-content/uploads/2024/04/7-1024x870.png)
  



Key Takeaways: Ethernaut Level 5
--------------------------------


* **Integer Underflow/Overflow:** Always be mindful of potential underflows and overflows when dealing with unsigned integers. Implement safeguards to prevent them. If you must use version 0.6.0, explore using tools like SafeMath. Now outdated, these concepts are important to know.


* **Security Mindset:** Even seemingly basic contracts can have hidden vulnerabilities. A security mindset during development is paramount. You can always do more research, consult experts, and practice writing secure code. Staying up-to-date on best practices and ensuring your own security mindset is the best preventive measure.


Ready for the next Ethernaut challenge? Click to check out the [previous ethernaut challenge](https://metana.io/blog/ethernaut-level-4-walkthrough-telephone) and see what’s [next](https://metana.io/blog/ethernaut-level-5-walkthrough-token/) in our series!



![faq](https://metana.io/wp-content/uploads/2024/01/Questions-cuate-1024x1024.png)
FAQs
----


**What is Ethernaut Level 5: Token about?**


* It is a blockchain-based puzzle involving smart contract manipulation to progress through levels in the Ethernaut game.


**How can I solve Ethernaut Challenge 5: Token?**


* Solving Level 5 requires understanding Ethereum smart contracts, specifically how token balances are managed and manipulated.


**What skills are necessary to complete Ethernaut Level 5?**


* Players need a basic understanding of Ethereum, smart contracts, and potentially some knowledge of Solidity programming.


**Are there any tools that help in solving Ethernaut Level 5?**


* Tools like Remix, MetaMask, and Solidity compilers are essential for interacting with and testing Ethereum smart contracts.


**What common mistakes should you avoid in Ethernaut Level 5?**


* Common mistakes include not verifying contract details thoroughly and misunderstanding the contract’s functions and permissions.






![](https://metana.io/wp-content/uploads/2024/05/Ethernaut-Level-5-Walkthrough-Token.avif) 





[PrevPreviousDAO Treasury Management](https://metana.io/blog/dao-treasury-management/) 




[NextEthernaut Level 6 Walkthrough: DelegationNext](https://metana.io/blog/ethernaut-level-6-walkthrough-delegation/) 







#### Metana Guarantees  a Job 💼

 





#### Plus Risk Free 2-Week Refund Policy ✨

 




 You’re guaranteed a new job in web3—or you’ll get a full tuition refund. We also offer a hassle-free two-week refund policy. If you’re not satisfied with your purchase for any reason, you can request a refund, no questions asked.

 






Web3 Solidity Bootcamp
======================

 





 The most advanced Solidity curriculum on the internet!

 




* 4 Months
* Prior coding experience required
* 20h/ Week
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-solidity-bootcamp-ethereum-blockchain/)







Full Stack Web3 Beginner Bootcamp
=================================

 





 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




* 7 Months
* Beginner - Zero to Hero
* 25h/ Week
* Your very own personal support tutor
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-beginner-bootcamp/)













You may also like
-----------------

 






![](https://metana.io/wp-content/uploads/2024/07/Protect-Yourself-from-Rug-Pulls-Tips-to-Avoid-Crypto-Scams-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




11 mins ago

#### [Protect Yourself from Rug Pulls: Tips to Avoid Crypto Scams](https://metana.io/blog/protect-yourself-from-rug-pulls-tips-to-avoid-crypto-scams/)




The world of Web3 is brimming with promises of high returns and revolutionary projects, driving 


![](https://metana.io/wp-content/uploads/2024/07/ERC-Token-Standards-Your-Simplified-Guide-copy-640x364.jpg)







### [Metana Editorial](https://metana.io/blog/author/editorial/)




1 day ago

#### [Address Poisoning in Smart Contracts](https://metana.io/blog/address-poisoning-in-smart-contracts/)




Web3 thrives on user empowerment and the ease of sending and receiving cryptocurrency. However, a 
 







#### Metana Guarantees  a Job 💼

 





#### Plus Risk Free 2-Week Refund Policy

 




You’re guaranteed a new job in web3—or you’ll get a full tuition refund. We also offer a hassle-free two-week refund policy. If you’re not satisfied with your purchase for any reason, you can request a refund, no questions asked.

 






#### Web3 Solidity Bootcamp

 





 The most advanced Solidity curriculum on the internet

 




* 4 Months
* Prior coding experience required
* 20h/ Week
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services






[View Program](/web3-solidity-bootcamp-ethereum-blockchain/)







Full Stack Web3 Beginner Bootcamp
=================================

 





 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




* 7 Months
* Beginner - Zero to Hero
* 25h/ Week
* Your very own personal support tutor
* 1-on-1 mentorship
* Expert code reviews
* Coaching & career services







 Learn foundational principles while gaining hands-on experience with Ethereum, DeFi, and Solidity.

 




[View Program](/web3-beginner-bootcamp/)







Events by Metana
================

 





 Dive into the exciting world of Web3 with us as we explore cutting-edge technical topics, provide valuable insights into the job market landscape, and offer guidance on securing lucrative positions in Web3. 

 




 





 







Do you have anything you want us to cover in our blog posts? What should we talk about next? We need your suggestions! 
 





Submit
















Start Your  Application
-----------------------

 






Secure your spot now. Spots are limited, and we accept qualified applicants on a first come, first served basis..




 






Email(Required)

Career Track(Required)


Web3



Data



Full Stack



Cyber

  








Δ










The application is free and takes just 3 minutes to complete.

 















##### What is included in the course?

 






### Expert-curated curriculum










### Weekly 1:1 video calls with your mentor










### Weekly group mentoring calls










### On-demand mentor support










### Portfolio reviews by Design hiring managers










### Resume & LinkedIn profile reviews










### Active online student community










### 1:1 and group career coaching calls










### Access to our employer network










### Job Guarantee




















 






###### Address

 





 44 Montgomery St,   

San Francisco, CA 94104, United States

 












Email 







Subscribe












###### Contact us

 





###### Call us directly

 





 (415) 416-0800

 





###### Mail us directly

 





 [[email protected]](/cdn-cgi/l/email-protection)

 









### Company

 




* [Home](/)
* [Blog](https://metana.io/blog/)
* [Jobs at Metana](/jobs/)
* [Bootcamp Application](https://metana.io/apply/)
* [Refer a friend](/refer/)
* [Student Perks](/perks/)
* [Testimonials](/reviews)
* [LMS login](https://app.metana.io/)
* [Open LMS login (Full Stack)](https://open.metana.io/)









### Bootcamp

 




* [Web3 Bootcamps](https://metana.io/web3-0-bootcamp/)
* [- Solidity Bootcamp](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [- Web3 Beginner Bootcamp](https://metana.io/web3-solidity-bootcamp-ethereum-blockchain/)
* [- Rust Bootcamp](https://metana.io/web3-rust-bootcamp-solana-blockchain/)
* [- ZK Bootcamp](/web3-zero-knowledge-bootcamp/)
* [Data + AI bootcamps](#)
* [- Data Analytics Bootcamp](/data-analytics-bootcamp/)
* [- Data Science Bootcamp](/data-science-bootcamp/)
* [- AI/ML Bootcamp](/ai-machine-learning-bootcamp/)
* [Software Engineering Bootcamp](/full-stack-software-engineer-bootcamp/)
* [Cybersecurity Bootcamp](/cybersecurity-bootcamp/)
* [Jobcamp](/jobcamp/)
* [Tuition](https://metana.io/tuition/)









### For businesses

 




* [Business](https://metana.io/business/)
* [- Hiring Partner](https://metana.io/business/hiring-partner/)
* [- Upskill Your Team](/business/upskill-your-team/)









### Legal

 




* [Licences](https://metana.io/licences/)
* [Metana's Job Guarantee](https://metana.io/job-guarantee/)
* [Withdrawal and Refund Policy](https://metana.io/withdrawal-and-refund-policy/)
* [Privacy Policy](/privacy-policy/)













[Still Unsure?](https://formless.ai/c/6bPi6ASGJ4ge)








[![](https://metana.io/wp-content/uploads/2022/07/Metana-Logo-Black-Full.png)](https://metana.io) 







 Disclaimer:
‍
Metana is involved in the Blockchain Education activities only. We are not dealing with any Crypto related stuff nor provide advice in the Crypto related field.

 

















 Metana is a pioneer in education and career transformation, specializing in today’s most in-demand skills. The leading source for training, staffing, and career transitions, we foster a flourishing community of professionals pursuing careers they love.
| © 2023 Edmore (private) limited

 








[Facebook](https://www.facebook.com/metanahq) 





[Linkedin](https://www.linkedin.com/school/metana/) 














































































Adding {{itemName}} to cart


Added {{itemName}} to cart













Loading...



×






