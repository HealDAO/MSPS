# MSPS (Medical Standards Proposal System)

## Mission

The core aim of this project is to develop a standardized format to minimize storage space required for medical and dental records. As the health care sector continues to digitalize, there's an increasing need to store vast amounts of patient data. However, space, especially on distributed systems, is limited and can be costly. Reducing the size of these records, without sacrificing data quality or accessibility, can lead to more efficient storage solutions and potentially faster data processing.

## Purpose

The MSPS is an addition to HealDAO, ensuring that medical standards are up-to-date, relevant, and universally recognized. By integrating it into the DAO's governance mechanism, it creates a holistic ecosystem where stakeholders not only manage health records but also actively shape the standards that govern them. This approach fosters community engagement, transparency, and continuous improvement.

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

## How to Use

### Decompression
To convert minified data to its expanded form:

1. Obtain output from the HealDAO contract; ensure the output is in JSON format.
2. You can either save this output to a file or pipe it directly into the `decompress.py` script.
   
```zsh
% # Reading from a file
% python decompress.py -i ./test/sample.json   

% # Using piping
% cat ./test/sample.json | python decompress.py
```

3. By default, the decompressed data will be printed to the console. If you'd like to save it to a file, use the `-o` or `--output-file` argument.
```zsh
% python decompress.py -i ./test/sample.json -o ./test/sample_decompressed.json
```

4. Verify the data's integrity by examining the printed `Abbreviation Hash`. This hash should match the hash provided in the HealDAO contract to ensure the accuracy of the expansion process.

### Compression
To convert expanded data back to its minified form:

1. Prepare the expanded data in a JSON format.
2. Use the `compress.py` script to process the data:

```zsh
% # Reading from a file
% python compress.py -i ./test/sample_decompressed.json

% # Using piping
% cat ./test/sample_decompressed.json | python compress.py
```

3. The script will generate a minified representation and print it to the console. Again, use the `-o` argument if you want to save this minified output to a file.
4. Check the `Abbreviation Hash` provided to ensure the minification was successful and maintains data integrity.

## Verification Mechanism

### Mathematical Proof using Ordered Hashes

Each minified or expanded piece of data is paired with an `Abbreviation Hash`. This hash is generated by taking the MD5 of the ordered set of abbreviations used in the data. By maintaining the same order, we ensure that the same set of abbreviations will always produce the same hash. This consistent mechanism helps in verifying the integrity and authenticity of the data at both ends.

**For Decompressed-to-Compressed Data:** When data is decompressed, the resulting expanded form is run through a hashing process that considers the abbreviations used in the data. This hash should align with the expected hash from the original source, offering a mathematical proof of the data's accurate expansion.

**For Compressed-to-Decompressed Data:** Similarly, when data is compressed, the hashing mechanism ensures that the minified data corresponds to its expanded counterpart, ensuring that no information is lost or misrepresented in the minification process.

This approach provides a reliable and mathematically robust mechanism to ensure that data, whether being compressed or decompressed, remains consistent and true to its original representation.

## Data Directory Breakdown

The `data` directory contains several JSON files, each tailored to specific aspects of medical and dental records. Here's a brief breakdown:

- **dx.json:** Contains medical and dental diagnoses. Each diagnosis is associated with a unique abbreviation to minimize space.
  
- **lx.json:** Specifies locations data, both medical and dental, such as teeth numberings, etc.
  
- **tx.json:** Enumerates treatments, both medical and dental, and assigns a unique abbreviation to each.
  
- **ax.json:** Lists common allergies and provides abbreviated codes for efficient storage.
  
- **ux.json:** Highlights units, such as measurement units used in vitals or bloodwork. Each unit has a short code.
  
- **bx.json:** Outlines standard bloodwork parameters, each associated with a unique identifier.
  
- **fx.json:** Encapsulates lifestyle factors, offering insights into habits or conditions that might impact health.
  
- **rx.json:** Details prescriptions, providing a short code for each drug and its related information.
  
- **vx.json:** Enumerates vital signs and other parameters that are essential for patient monitoring, again using unique abbreviations for efficient storage.

For more details on the abbreviations and their respective mappings, refer to the individual JSON files.
