# /feature - End-to-End Feature Development

**Purpose**: Orchestrate the end-to-end development of a complete feature, from requirements analysis to implementation and testing.

## Usage
```bash
/feature "add user profile management"
/feature "implement shopping cart functionality"
/feature "create admin dashboard"
/feature "add real-time notifications"
```

## Workflow

The `/feature` command orchestrates the complete feature development lifecycle.

```xml
<feature_workflow>
  <step name="Requirements Analysis">
    <description>Define the feature's scope, components, and functional/non-functional requirements. Create a clear specification to guide development.</description>
    <output>A detailed feature specification document.</output>
  </step>
  
  <step name="Architecture Design">
    <description>Plan the components, data models, API endpoints, and integration points for the new feature. This includes frontend, backend, and database architecture.</description>
    <output>An architectural plan outlining all necessary components.</output>
  </step>
  
  <step name="Parallel Implementation">
    <description>Build the various components of the feature in parallel to maximize efficiency. This includes creating backend models and services, frontend components and state management, and database migrations.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create all necessary files for the feature in parallel.</description>
    </tool_usage>
  </step>
  
  <step name="Integration & Dependency Management">
    <description>Connect the newly created components, install any necessary dependencies, and ensure that all parts of the feature work together seamlessly.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run dependency installation commands (e.g., 'npm install') and database migrations.</description>
    </tool_usage>
  </step>
  
  <step name="Testing & Validation">
    <description>Create and run a comprehensive suite of tests, including unit, integration, and end-to-end tests, to ensure the feature is working correctly and meets all quality standards.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create test files for the new feature.</description>
      <tool>Bash</tool>
      <description>Run the project's test suite.</description>
    </tool_usage>
  </step>
</feature_workflow>
```

## Feature Development Process

### 1. Requirements Gathering
```javascript
// Analyze feature request
const featureSpec = {
  name: "User Profile Management",
  components: [
    "Profile model/schema",
    "API endpoints (CRUD)",
    "Frontend views",
    "Form validation",
    "Image upload handling",
    "Privacy settings"
  ],
  requirements: {
    functional: ["View profile", "Edit profile", "Upload avatar"],
    nonFunctional: ["Mobile responsive", "Fast loading", "Secure"]
  }
};
```

### 2. Architecture Planning
```javascript
// Component architecture
const architecture = {
  backend: {
    models: ["User", "Profile", "ProfileSettings"],
    services: ["ProfileService", "ImageUploadService"],
    controllers: ["ProfileController"],
    routes: ["/api/profile/*"],
    middleware: ["auth", "validateProfile", "imageProcessor"]
  },
  frontend: {
    pages: ["ProfileView", "ProfileEdit"],
    components: ["ProfileCard", "AvatarUpload", "ProfileForm"],
    state: ["profileStore", "profileActions"],
    api: ["profileAPI"]
  },
  database: {
    migrations: ["add_profile_table", "add_avatar_column"],
    indexes: ["user_id_index", "username_index"]
  }
};
```

### 3. Parallel Implementation
```javascript
// Execute component creation in parallel
const implementations = await Promise.all([
  // Backend components
  createBackendComponents(architecture.backend),
  
  // Frontend components
  createFrontendComponents(architecture.frontend),
  
  // Database setup
  setupDatabase(architecture.database),
  
  // Test scaffolding
  createTestSuite(featureSpec)
]);
```

## Implementation Examples

### Backend Implementation
```javascript
// Create model
await Write('src/models/Profile.js', `
class Profile extends Model {
  static schema = {
    userId: { type: 'string', required: true, unique: true },
    displayName: { type: 'string', required: true },
    bio: { type: 'string', maxLength: 500 },
    avatar: { type: 'string' },
    settings: { type: 'json' },
    createdAt: { type: 'datetime', default: Date.now },
    updatedAt: { type: 'datetime', default: Date.now }
  };
  
  static associations = {
    user: { type: 'belongsTo', model: 'User' }
  };
}
`);

// Create service layer
await Write('src/services/ProfileService.js', `
class ProfileService {
  async getProfile(userId) {
    const profile = await Profile.findOne({ userId });
    if (!profile) {
      throw new NotFoundError('Profile not found');
    }
    return profile;
  }
  
  async updateProfile(userId, data) {
    const validation = validateProfileData(data);
    if (!validation.valid) {
      throw new ValidationError(validation.errors);
    }
    
    return await Profile.update({ userId }, {
      ...data,
      updatedAt: new Date()
    });
  }
}
`);

// Create API routes
await Write('src/routes/profile.js', `
router.get('/api/profile/:userId', auth, async (req, res) => {
  try {
    const profile = await profileService.getProfile(req.params.userId);
    res.json({ success: true, profile });
  } catch (error) {
    res.status(error.status || 500).json({ 
      success: false, 
      error: error.message 
    });
  }
});

router.put('/api/profile', auth, validateProfile, async (req, res) => {
  try {
    const profile = await profileService.updateProfile(
      req.user.id, 
      req.body
    );
    res.json({ success: true, profile });
  } catch (error) {
    res.status(error.status || 500).json({ 
      success: false, 
      error: error.message 
    });
  }
});
`);
```

### Frontend Implementation
```javascript
// Create React component
await Write('src/components/ProfileView.jsx', `
import React, { useEffect, useState } from 'react';
import { useProfile } from '../hooks/useProfile';
import { ProfileCard } from './ProfileCard';
import { LoadingSpinner } from './LoadingSpinner';

export function ProfileView({ userId }) {
  const { profile, loading, error } = useProfile(userId);
  
  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;
  
  return (
    <div className="profile-view">
      <ProfileCard profile={profile} />
      {profile.isOwner && (
        <Link to="/profile/edit" className="edit-button">
          Edit Profile
        </Link>
      )}
    </div>
  );
}
`);

// Create state management
await Write('src/store/profileStore.js', `
import { create } from 'zustand';
import { profileAPI } from '../api/profile';

export const useProfileStore = create((set, get) => ({
  profile: null,
  loading: false,
  error: null,
  
  fetchProfile: async (userId) => {
    set({ loading: true, error: null });
    try {
      const profile = await profileAPI.getProfile(userId);
      set({ profile, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
  
  updateProfile: async (data) => {
    set({ loading: true });
    try {
      const updated = await profileAPI.updateProfile(data);
      set({ profile: updated, loading: false });
      return { success: true };
    } catch (error) {
      set({ error: error.message, loading: false });
      return { success: false, error };
    }
  }
}));
`);
```

### Testing Implementation
```javascript
// Integration tests
await Write('__tests__/features/profile.test.js', `
describe('Profile Feature', () => {
  describe('API Endpoints', () => {
    it('should fetch user profile', async () => {
      const user = await createTestUser();
      const response = await request(app)
        .get(\`/api/profile/\${user.id}\`)
        .set('Authorization', \`Bearer \${user.token}\`);
        
      expect(response.status).toBe(200);
      expect(response.body.profile).toMatchObject({
        userId: user.id,
        displayName: user.name
      });
    });
    
    it('should update profile with validation', async () => {
      const user = await createTestUser();
      const updates = { bio: 'New bio', displayName: 'New Name' };
      
      const response = await request(app)
        .put('/api/profile')
        .set('Authorization', \`Bearer \${user.token}\`)
        .send(updates);
        
      expect(response.status).toBe(200);
      expect(response.body.profile.bio).toBe(updates.bio);
    });
  });
  
  describe('Frontend Components', () => {
    it('should render profile view', () => {
      const profile = createMockProfile();
      const { getByText } = render(<ProfileView profile={profile} />);
      
      expect(getByText(profile.displayName)).toBeInTheDocument();
      expect(getByText(profile.bio)).toBeInTheDocument();
    });
  });
});
`);
```

## Intelligent Orchestration

### Dependency Management
```javascript
// Identify and resolve dependencies
const dependencies = {
  frontend: ['react', 'zustand', 'axios'],
  backend: ['express', 'multer', 'sharp'],
  testing: ['jest', 'supertest', '@testing-library/react']
};

// Install in parallel
await Promise.all([
  Bash('npm install ' + dependencies.frontend.join(' ')),
  Bash('npm install ' + dependencies.backend.join(' ')),
  Bash('npm install -D ' + dependencies.testing.join(' '))
]);
```

### Migration and Setup
```javascript
// Database migrations
await Write('migrations/001_create_profile_table.sql', `
CREATE TABLE profiles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL UNIQUE REFERENCES users(id),
  display_name VARCHAR(100) NOT NULL,
  bio TEXT,
  avatar_url VARCHAR(500),
  settings JSONB DEFAULT '{}',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_profiles_user_id ON profiles(user_id);
`);

// Run migration
await Bash('npm run migrate');
```

## Configuration

Customize behavior via `PROJECT_CONFIG.xml`:
```xml
<project_config>
  <commands>
    <feature>
      <parallel_components>true</parallel_components>
      <auto_install_deps>true</auto_install_deps>
      <generate_tests>true</generate_tests>
      <test_coverage_threshold>80</test_coverage_threshold>
      <documentation>true</documentation>
      <style_guide>airbnb</style_guide>
    </feature>
  </commands>
</project_config>
```

## Best Practices

1. **Plan Before Building** - Architecture prevents rework.
2. **Build in Parallel** - Leverage parallel execution.
3. **Test Everything** - Integration + unit tests.
4. **Document APIs** - Clear contracts between components.
5. **Consider Edge Cases** - Error handling, validation.
6. **Performance First** - Optimize from the start.

---
*Building complete features with architectural excellence*