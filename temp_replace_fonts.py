import os
import glob

# List of files to update
files = [
    'src/app/components/StyleDNASection.tsx',
    'src/app/components/ContentGenerationSection.tsx',
    'src/app/components/AudienceSection.tsx',
    'src/app/components/WorkflowComparisonSection.tsx',
    'src/app/components/IntegrationsSection.tsx',
    'src/app/components/WorkflowProcessSection.tsx',
    'src/app/components/SocialProofSection.tsx',
    'src/app/components/FinalCTASection.tsx',
    'src/app/components/Footer.tsx',
    'src/app/components/FeaturesSection.tsx',
    'src/app/components/UseCasesSection.tsx',
    'src/app/components/CTASection.tsx',
]

for filepath in files:
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Replace Plus Jakarta Sans with DM Sans
        updated_content = content.replace('Plus Jakarta Sans', 'DM Sans')
        
        with open(filepath, 'w') as file:
            file.write(updated_content)
        
        print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

print("All files processed!")
