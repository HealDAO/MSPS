# MSPS (Medical Standards Proposal System)

## Mission

The core aim of this project is to develop a standardized format to minimize storage space required for medical and dental records. As the health care sector continues to digitalize, there's an increasing need to store vast amounts of patient data. However, space, especially on distributed systems, is limited and can be costly. Reducing the size of these records, without sacrificing data quality or accessibility, can lead to more efficient storage solutions and potentially faster data processing.

## Purpose

The MSPS is a powerful addition to HealDAO, ensuring that medical standards are up-to-date, relevant, and universally recognized. By integrating it into the DAO's governance mechanism, it creates a holistic ecosystem where stakeholders not only manage health records but also actively shape the standards that govern them. This approach fosters community engagement, transparency, and continuous improvement.

1. **Components**:

   a. **Proposal Submission**:
      - Allows users to submit new abbreviations, standards, or changes to existing ones.
      - Each proposal should include a detailed description, rationale, and any supporting documentation or references.

   b. **Discussion Forum**:
      - A platform for stakeholders to discuss, debate, and provide feedback on proposals.
      - This can be integrated with existing discussion platforms or built as a custom solution.

   c. **Voting Mechanism**:
      - Allows stakeholders to vote on proposals.
      - Voting can be based on token holdings, reputation, or other criteria to ensure informed decision-making.

   d. **Implementation & Recording**:
      - Once a proposal is approved, it's implemented into the system.
      - The proposal's details, discussions, and voting results are recorded on the blockchain for transparency and immutability.

2. **Workflow**:

   a. **Submission**:
      - A user submits a proposal for a new standard or change.
   
   b. **Review Period**:
      - A predefined period during which stakeholders can review the proposal, ask questions, and provide feedback.
   
   c. **Voting Period**:
      - Stakeholders vote on the proposal.
      - The voting mechanism can be simple (majority wins) or more complex (weighted voting based on reputation, etc.).
   
   d. **Implementation**:
      - If approved, the proposal is implemented.
      - If rejected, feedback is provided to the proposer, who can make revisions and resubmit.

3. **Governance**:

   a. **Roles & Responsibilities**:
      - **Proposers**: Submit new proposals.
      - **Reviewers**: Medical professionals or experts who review proposals for accuracy and relevance.
      - **Voters**: Stakeholders who vote on proposals.
      - **Administrators**: Oversee the platform, ensure smooth operations, and handle disputes.

   b. **Incentives**:
      - Consider introducing incentives for active participation, such as token rewards for proposal submission, review, and voting.

   c. **Dispute Resolution**:
      - Establish a mechanism to handle disputes, disagreements, or challenges to decisions.

4. **Integration with HealthRecordsDAO**:
   
   a. **Linkage**:
      - The MSPS can be linked to the main DAO, allowing for seamless integration of approved standards into the HealthRecordsDAO system.
   
   b. **Data Verification**:
      - As discussed earlier, use cryptographic hashing to verify the integrity of data conversions based on the approved standards.

## Why Minimization is Necessary

1. **Cost-Effective Storage:** Reducing the size of records means more data can be stored at a lesser cost. This becomes critical when considering long-term data retention requirements.
  
2. **Efficient Data Processing:** Smaller data sets can be processed faster, especially important for critical applications where time is of the essence, such as in emergency medical situations.
  
3. **Optimized Data Transmission:** Transmitting smaller packets of data is faster and can be particularly beneficial for telemedicine applications or when accessing cloud-based records.
  
4. **Scalability:** As the number of patients grows, so does the need for storage. A minimized storage requirement ensures the system remains scalable.
  
5. **Environmental Impact:** Data centers consume a significant amount of power. Reducing the data storage footprint can contribute to reduced energy consumption.

## Data Directory Breakdown

The `data` directory contains several JSON files, each tailored to specific aspects of medical and dental records. Here's a brief breakdown:

- **dxD.json:** Contains dental diagnoses. Each diagnosis is associated with a unique abbreviation to minimize space.
  
- **lxD.json:** Specifies locations within the dental context. It aids in identifying specific parts of the oral cavity where a diagnosis or treatment is relevant.
  
- **tx.json:** Enumerates treatments, both medical and dental, and assigns a unique abbreviation to each.
  
- **ax.json:** Lists common allergies and provides abbreviated codes for efficient storage.
  
- **dxM.json:** Focuses on medical diagnoses, providing concise codes for a broad spectrum of medical conditions.
  
- **lxM.json:** Defines locations within a medical context. This helps pinpoint where a particular diagnosis or treatment took place on the body.
  
- **ux.json:** Highlights units, such as measurement units used in vitals or bloodwork. Each unit has a short code.
  
- **bx.json:** Outlines standard bloodwork parameters, each associated with a unique identifier.
  
- **fx.json:** Encapsulates lifestyle factors, offering insights into habits or conditions that might impact health.
  
- **rx.json:** Details prescriptions, providing a short code for each drug and its related information.
  
- **vx.json:** Enumerates vital signs and other parameters that are essential for patient monitoring, again using unique abbreviations for efficient storage.

For more details on the abbreviations and their respective mappings, refer to the individual JSON files.
