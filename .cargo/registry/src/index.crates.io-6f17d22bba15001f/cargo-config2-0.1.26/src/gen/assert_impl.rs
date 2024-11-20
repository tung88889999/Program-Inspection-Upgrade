// SPDX-License-Identifier: Apache-2.0 OR MIT
// This file is @generated by cargo-config2-internal-codegen
// (gen_assert_impl function at tools/codegen/src/main.rs).
// It is not intended for manual editing.

#![cfg_attr(rustfmt, rustfmt::skip)]
#![allow(
    dead_code,
    unused_macros,
    clippy::std_instead_of_alloc,
    clippy::std_instead_of_core,
)]
fn assert_send<T: ?Sized + Send>() {}
fn assert_sync<T: ?Sized + Sync>() {}
fn assert_unpin<T: ?Sized + Unpin>() {}
fn assert_unwind_safe<T: ?Sized + std::panic::UnwindSafe>() {}
fn assert_ref_unwind_safe<T: ?Sized + std::panic::RefUnwindSafe>() {}
/// `Send` & `!Sync`
struct NotSync(core::cell::UnsafeCell<()>);
/// `!Send` & `Sync`
struct NotSend(std::sync::MutexGuard<'static, ()>);
/// `!Send` & `!Sync`
struct NotSendSync(*const ());
/// `!Unpin`
struct NotUnpin(core::marker::PhantomPinned);
/// `!UnwindSafe`
struct NotUnwindSafe(&'static mut ());
/// `!RefUnwindSafe`
struct NotRefUnwindSafe(core::cell::UnsafeCell<()>);
macro_rules! assert_not_send {
    ($ty:ty) => {
        static_assertions::assert_not_impl_all!($ty : Send);
    };
}
macro_rules! assert_not_sync {
    ($ty:ty) => {
        static_assertions::assert_not_impl_all!($ty : Sync);
    };
}
macro_rules! assert_not_unpin {
    ($ty:ty) => {
        static_assertions::assert_not_impl_all!($ty : Unpin);
    };
}
macro_rules! assert_not_unwind_safe {
    ($ty:ty) => {
        static_assertions::assert_not_impl_all!($ty : std::panic::UnwindSafe);
    };
}
macro_rules! assert_not_ref_unwind_safe {
    ($ty:ty) => {
        static_assertions::assert_not_impl_all!($ty : std::panic::RefUnwindSafe);
    };
}
const _: fn() = || {
    assert_send::<crate::de::Config>();
    assert_sync::<crate::de::Config>();
    assert_unpin::<crate::de::Config>();
    assert_unwind_safe::<crate::de::Config>();
    assert_ref_unwind_safe::<crate::de::Config>();
    assert_send::<crate::de::BuildConfig>();
    assert_sync::<crate::de::BuildConfig>();
    assert_unpin::<crate::de::BuildConfig>();
    assert_unwind_safe::<crate::de::BuildConfig>();
    assert_ref_unwind_safe::<crate::de::BuildConfig>();
    assert_send::<crate::de::TargetConfig>();
    assert_sync::<crate::de::TargetConfig>();
    assert_unpin::<crate::de::TargetConfig>();
    assert_unwind_safe::<crate::de::TargetConfig>();
    assert_ref_unwind_safe::<crate::de::TargetConfig>();
    assert_send::<crate::de::DocConfig>();
    assert_sync::<crate::de::DocConfig>();
    assert_unpin::<crate::de::DocConfig>();
    assert_unwind_safe::<crate::de::DocConfig>();
    assert_ref_unwind_safe::<crate::de::DocConfig>();
    assert_send::<crate::de::EnvConfigValue>();
    assert_sync::<crate::de::EnvConfigValue>();
    assert_unpin::<crate::de::EnvConfigValue>();
    assert_unwind_safe::<crate::de::EnvConfigValue>();
    assert_ref_unwind_safe::<crate::de::EnvConfigValue>();
    assert_send::<crate::de::FutureIncompatReportConfig>();
    assert_sync::<crate::de::FutureIncompatReportConfig>();
    assert_unpin::<crate::de::FutureIncompatReportConfig>();
    assert_unwind_safe::<crate::de::FutureIncompatReportConfig>();
    assert_ref_unwind_safe::<crate::de::FutureIncompatReportConfig>();
    assert_send::<crate::de::NetConfig>();
    assert_sync::<crate::de::NetConfig>();
    assert_unpin::<crate::de::NetConfig>();
    assert_unwind_safe::<crate::de::NetConfig>();
    assert_ref_unwind_safe::<crate::de::NetConfig>();
    assert_send::<crate::de::RegistriesConfigValue>();
    assert_sync::<crate::de::RegistriesConfigValue>();
    assert_unpin::<crate::de::RegistriesConfigValue>();
    assert_unwind_safe::<crate::de::RegistriesConfigValue>();
    assert_ref_unwind_safe::<crate::de::RegistriesConfigValue>();
    assert_send::<crate::de::RegistriesProtocol>();
    assert_sync::<crate::de::RegistriesProtocol>();
    assert_unpin::<crate::de::RegistriesProtocol>();
    assert_unwind_safe::<crate::de::RegistriesProtocol>();
    assert_ref_unwind_safe::<crate::de::RegistriesProtocol>();
    assert_send::<crate::de::RegistryConfig>();
    assert_sync::<crate::de::RegistryConfig>();
    assert_unpin::<crate::de::RegistryConfig>();
    assert_unwind_safe::<crate::de::RegistryConfig>();
    assert_ref_unwind_safe::<crate::de::RegistryConfig>();
    assert_send::<crate::de::TermConfig>();
    assert_sync::<crate::de::TermConfig>();
    assert_unpin::<crate::de::TermConfig>();
    assert_unwind_safe::<crate::de::TermConfig>();
    assert_ref_unwind_safe::<crate::de::TermConfig>();
    assert_send::<crate::de::TermProgress>();
    assert_sync::<crate::de::TermProgress>();
    assert_unpin::<crate::de::TermProgress>();
    assert_unwind_safe::<crate::de::TermProgress>();
    assert_ref_unwind_safe::<crate::de::TermProgress>();
    assert_send::<crate::de::Color>();
    assert_sync::<crate::de::Color>();
    assert_unpin::<crate::de::Color>();
    assert_unwind_safe::<crate::de::Color>();
    assert_ref_unwind_safe::<crate::de::Color>();
    assert_send::<crate::de::When>();
    assert_sync::<crate::de::When>();
    assert_unpin::<crate::de::When>();
    assert_unwind_safe::<crate::de::When>();
    assert_ref_unwind_safe::<crate::de::When>();
    assert_send::<crate::de::Frequency>();
    assert_sync::<crate::de::Frequency>();
    assert_unpin::<crate::de::Frequency>();
    assert_unwind_safe::<crate::de::Frequency>();
    assert_ref_unwind_safe::<crate::de::Frequency>();
    assert_send::<crate::de::Flags>();
    assert_sync::<crate::de::Flags>();
    assert_unpin::<crate::de::Flags>();
    assert_unwind_safe::<crate::de::Flags>();
    assert_ref_unwind_safe::<crate::de::Flags>();
    assert_send::<crate::de::ConfigRelativePath>();
    assert_sync::<crate::de::ConfigRelativePath>();
    assert_unpin::<crate::de::ConfigRelativePath>();
    assert_unwind_safe::<crate::de::ConfigRelativePath>();
    assert_ref_unwind_safe::<crate::de::ConfigRelativePath>();
    assert_send::<crate::de::PathAndArgs>();
    assert_sync::<crate::de::PathAndArgs>();
    assert_unpin::<crate::de::PathAndArgs>();
    assert_unwind_safe::<crate::de::PathAndArgs>();
    assert_ref_unwind_safe::<crate::de::PathAndArgs>();
    assert_send::<crate::de::StringList>();
    assert_sync::<crate::de::StringList>();
    assert_unpin::<crate::de::StringList>();
    assert_unwind_safe::<crate::de::StringList>();
    assert_ref_unwind_safe::<crate::de::StringList>();
    assert_send::<crate::de::StringOrArray>();
    assert_sync::<crate::de::StringOrArray>();
    assert_unpin::<crate::de::StringOrArray>();
    assert_unwind_safe::<crate::de::StringOrArray>();
    assert_ref_unwind_safe::<crate::de::StringOrArray>();
    assert_send::<crate::easy::Config>();
    assert_not_sync!(crate::easy::Config);
    assert_unpin::<crate::easy::Config>();
    assert_unwind_safe::<crate::easy::Config>();
    assert_not_ref_unwind_safe!(crate::easy::Config);
    assert_send::<crate::easy::BuildConfig>();
    assert_sync::<crate::easy::BuildConfig>();
    assert_unpin::<crate::easy::BuildConfig>();
    assert_unwind_safe::<crate::easy::BuildConfig>();
    assert_ref_unwind_safe::<crate::easy::BuildConfig>();
    assert_send::<crate::easy::TargetConfig>();
    assert_sync::<crate::easy::TargetConfig>();
    assert_unpin::<crate::easy::TargetConfig>();
    assert_unwind_safe::<crate::easy::TargetConfig>();
    assert_ref_unwind_safe::<crate::easy::TargetConfig>();
    assert_send::<crate::easy::DocConfig>();
    assert_sync::<crate::easy::DocConfig>();
    assert_unpin::<crate::easy::DocConfig>();
    assert_unwind_safe::<crate::easy::DocConfig>();
    assert_ref_unwind_safe::<crate::easy::DocConfig>();
    assert_send::<crate::easy::EnvConfigValue>();
    assert_sync::<crate::easy::EnvConfigValue>();
    assert_unpin::<crate::easy::EnvConfigValue>();
    assert_unwind_safe::<crate::easy::EnvConfigValue>();
    assert_ref_unwind_safe::<crate::easy::EnvConfigValue>();
    assert_send::<crate::easy::FutureIncompatReportConfig>();
    assert_sync::<crate::easy::FutureIncompatReportConfig>();
    assert_unpin::<crate::easy::FutureIncompatReportConfig>();
    assert_unwind_safe::<crate::easy::FutureIncompatReportConfig>();
    assert_ref_unwind_safe::<crate::easy::FutureIncompatReportConfig>();
    assert_send::<crate::easy::NetConfig>();
    assert_sync::<crate::easy::NetConfig>();
    assert_unpin::<crate::easy::NetConfig>();
    assert_unwind_safe::<crate::easy::NetConfig>();
    assert_ref_unwind_safe::<crate::easy::NetConfig>();
    assert_send::<crate::easy::RegistriesConfigValue>();
    assert_sync::<crate::easy::RegistriesConfigValue>();
    assert_unpin::<crate::easy::RegistriesConfigValue>();
    assert_unwind_safe::<crate::easy::RegistriesConfigValue>();
    assert_ref_unwind_safe::<crate::easy::RegistriesConfigValue>();
    assert_send::<crate::easy::RegistryConfig>();
    assert_sync::<crate::easy::RegistryConfig>();
    assert_unpin::<crate::easy::RegistryConfig>();
    assert_unwind_safe::<crate::easy::RegistryConfig>();
    assert_ref_unwind_safe::<crate::easy::RegistryConfig>();
    assert_send::<crate::easy::TermConfig>();
    assert_sync::<crate::easy::TermConfig>();
    assert_unpin::<crate::easy::TermConfig>();
    assert_unwind_safe::<crate::easy::TermConfig>();
    assert_ref_unwind_safe::<crate::easy::TermConfig>();
    assert_send::<crate::easy::TermProgressConfig>();
    assert_sync::<crate::easy::TermProgressConfig>();
    assert_unpin::<crate::easy::TermProgressConfig>();
    assert_unwind_safe::<crate::easy::TermProgressConfig>();
    assert_ref_unwind_safe::<crate::easy::TermProgressConfig>();
    assert_send::<crate::easy::Flags>();
    assert_sync::<crate::easy::Flags>();
    assert_unpin::<crate::easy::Flags>();
    assert_unwind_safe::<crate::easy::Flags>();
    assert_ref_unwind_safe::<crate::easy::Flags>();
    assert_send::<crate::easy::PathAndArgs>();
    assert_sync::<crate::easy::PathAndArgs>();
    assert_unpin::<crate::easy::PathAndArgs>();
    assert_unwind_safe::<crate::easy::PathAndArgs>();
    assert_ref_unwind_safe::<crate::easy::PathAndArgs>();
    assert_send::<crate::easy::StringList>();
    assert_sync::<crate::easy::StringList>();
    assert_unpin::<crate::easy::StringList>();
    assert_unwind_safe::<crate::easy::StringList>();
    assert_ref_unwind_safe::<crate::easy::StringList>();
    assert_send::<crate::error::Error>();
    assert_sync::<crate::error::Error>();
    assert_unpin::<crate::error::Error>();
    assert_not_unwind_safe!(crate::error::Error);
    assert_not_ref_unwind_safe!(crate::error::Error);
    assert_send::<crate::resolve::ResolveOptions>();
    assert_sync::<crate::resolve::ResolveOptions>();
    assert_unpin::<crate::resolve::ResolveOptions>();
    assert_unwind_safe::<crate::resolve::ResolveOptions>();
    assert_ref_unwind_safe::<crate::resolve::ResolveOptions>();
    assert_send::<crate::resolve::ResolveContext>();
    assert_not_sync!(crate::resolve::ResolveContext);
    assert_unpin::<crate::resolve::ResolveContext>();
    assert_unwind_safe::<crate::resolve::ResolveContext>();
    assert_not_ref_unwind_safe!(crate::resolve::ResolveContext);
    assert_send::<crate::resolve::TargetTripleRef<'_>>();
    assert_sync::<crate::resolve::TargetTripleRef<'_>>();
    assert_unpin::<crate::resolve::TargetTripleRef<'_>>();
    assert_unwind_safe::<crate::resolve::TargetTripleRef<'_>>();
    assert_ref_unwind_safe::<crate::resolve::TargetTripleRef<'_>>();
    assert_send::<crate::resolve::TargetTriple>();
    assert_sync::<crate::resolve::TargetTriple>();
    assert_unpin::<crate::resolve::TargetTriple>();
    assert_unwind_safe::<crate::resolve::TargetTriple>();
    assert_ref_unwind_safe::<crate::resolve::TargetTriple>();
    assert_send::<crate::resolve::RustcVersion>();
    assert_sync::<crate::resolve::RustcVersion>();
    assert_unpin::<crate::resolve::RustcVersion>();
    assert_unwind_safe::<crate::resolve::RustcVersion>();
    assert_ref_unwind_safe::<crate::resolve::RustcVersion>();
    assert_send::<crate::resolve::CargoVersion>();
    assert_sync::<crate::resolve::CargoVersion>();
    assert_unpin::<crate::resolve::CargoVersion>();
    assert_unwind_safe::<crate::resolve::CargoVersion>();
    assert_ref_unwind_safe::<crate::resolve::CargoVersion>();
    assert_send::<crate::value::Value<()>>();
    assert_send::<crate::value::Value<NotSync>>();
    assert_not_send!(crate::value::Value<NotSend>);
    assert_sync::<crate::value::Value<()>>();
    assert_sync::<crate::value::Value<NotSend>>();
    assert_not_sync!(crate::value::Value<NotSync>);
    assert_unpin::<crate::value::Value<()>>();
    assert_not_unpin!(crate::value::Value<NotUnpin>);
    assert_unwind_safe::<crate::value::Value<()>>();
    assert_not_unwind_safe!(crate::value::Value<NotUnwindSafe>);
    assert_ref_unwind_safe::<crate::value::Value<()>>();
    assert_not_ref_unwind_safe!(crate::value::Value<NotRefUnwindSafe>);
    assert_send::<crate::value::Definition>();
    assert_sync::<crate::value::Definition>();
    assert_unpin::<crate::value::Definition>();
    assert_unwind_safe::<crate::value::Definition>();
    assert_ref_unwind_safe::<crate::value::Definition>();
    assert_send::<crate::walk::Walk<'_>>();
    assert_sync::<crate::walk::Walk<'_>>();
    assert_unpin::<crate::walk::Walk<'_>>();
    assert_unwind_safe::<crate::walk::Walk<'_>>();
    assert_ref_unwind_safe::<crate::walk::Walk<'_>>();
};