import { SITE_URL, GOOGLE_SITE_VERIFICATION, BING_SITE_VERIFICATION } from 'astro:env/server';

export interface SiteConfig {
  name: string;
  description: string;
  url: string;
  ogImage: string;
  author: string;
  email: string;
  phone?: string;
  address?: {
    street: string;
    city: string;
    state: string;
    zip: string;
    country: string;
  };
  socialLinks: string[];
  twitter?: {
    site: string;
    creator: string;
  };
  verification?: {
    google?: string;
    bing?: string;
  };
  branding: {
    logo: {
      alt: string;
    };
    favicon: {
      svg: string;
    };
    colors: {
      themeColor: string;
      backgroundColor: string;
    };
  };
}

const siteConfig: SiteConfig = {
  name: 'Kamal Rupareliya',
  description: 'Ideas, insights and stories.',
  url: SITE_URL || 'https://k.rupareliya.com',
  ogImage: '/og-default.png',
  author: 'Kamal Rupareliya',
  email: 'hello@rupareliya.com',
  socialLinks: [
    'https://github.com/kamalrupareliya',
    'https://twitter.com/kamalrupareliya',
    'https://www.linkedin.com/in/kamalrupareliya',
  ],
  twitter: {
    site: '@kamalrupareliya',
    creator: '@kamalrupareliya',
  },
  verification: {
    google: GOOGLE_SITE_VERIFICATION,
    bing: BING_SITE_VERIFICATION,
  },
  branding: {
    logo: {
      alt: 'Kamal Rupareliya',
    },
    favicon: {
      svg: '/favicon.svg',
    },
    colors: {
      themeColor: '#965496',
      backgroundColor: '#FAFBFC',
    },
  },
};

export default siteConfig;
