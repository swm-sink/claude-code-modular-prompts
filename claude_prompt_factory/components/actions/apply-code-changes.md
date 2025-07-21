<prompt_component>
  <step name="Apply Code Changes">
    <description>
      Carefully apply the changes as described in the approved plan.
      You must ensure that the modifications are implemented correctly and do not introduce any new errors.
      Apply the changes by generating the precise code edits for the target files.
    </description>
    <safeguards>
      <safeguard>Do not modify any code outside the scope of the approved plan.</safeguard>
      <safeguard>Validate the code after changes to ensure it is still syntactically correct.</safeguard>
      <safeguard>If possible, run the relevant tests using the `${scripts.script#test:unit}` command to verify the changes.</safeguard>
    </safeguards>
    <output>
      Provide a summary of the changes that were applied.
    </output>
  </step>
</prompt_component> 