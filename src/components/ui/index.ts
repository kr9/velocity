/**
 * UI Component Exports
 *
 * This file exports React components for use with Astro's client:* directives.
 * React components are needed for interactive client-side functionality.
 *
 * Astro components (*.astro) are imported directly from their files:
 * - Badge.astro, Alert.astro, Tabs.astro, Dropdown.astro, Dialog.astro
 * - Tooltip.astro, Avatar.astro, AvatarGroup.astro, Skeleton.astro, Icon.astro
 * - Button.astro (server-side), CTA.astro, NpmCopyButton.astro, Logo.astro
 * - Separator.astro, Switch.astro, Accordion.astro, Progress.astro
 * - Table.astro, Pagination.astro
 */

// React components for client-side interactivity
export { Button } from './Button';
export { Input } from './Input';
export { Textarea } from './Textarea';
export { Select } from './Select';
export { Checkbox } from './Checkbox';
export { Radio } from './Radio';
export { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from './Card';
export { VerticalTabs, type VerticalTab } from './VerticalTabs';
export { Switch } from './Switch';
export { ToastProvider, useToast } from './Toast';

// Shared variant definitions (importable by users for extension)
export { buttonVariants, type ButtonVariants } from './button.variants';
export { badgeVariants, type BadgeVariants } from './badge.variants';
export { inputVariants, inputSizeConfig, type InputVariants } from './input.variants';
export { cardVariants, type CardVariants } from './card.variants';
export { alertVariants, alertIconColors, alertAccentColors, type AlertVariants } from './alert.variants';
export { selectVariants, type SelectVariants } from './select.variants';
export { textareaVariants, type TextareaVariants } from './textarea.variants';
export { checkboxBoxVariants, type CheckboxVariants } from './checkbox.variants';
export { radioCircleVariants, radioCardVariants, type RadioVariants } from './radio.variants';
export { skeletonVariants, type SkeletonVariants } from './skeleton.variants';
export { avatarVariants, type AvatarVariants } from './avatar.variants';
export { separatorVariants, type SeparatorVariants } from './separator.variants';
export { switchTrackVariants, switchThumbVariants, type SwitchVariants } from './switch.variants';
export { accordionItemVariants, accordionTriggerVariants, type AccordionVariants } from './accordion.variants';
export { toastVariants, toastIconColors, type ToastVariants } from './toast.variants';
export { progressTrackVariants, progressBarVariants, type ProgressVariants } from './progress.variants';
export { paginationItemVariants, type PaginationVariants } from './pagination.variants';
