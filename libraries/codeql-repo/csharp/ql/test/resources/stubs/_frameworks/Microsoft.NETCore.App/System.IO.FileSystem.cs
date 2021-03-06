// This file contains auto-generated code.

namespace System
{
    namespace IO
    {
        // Generated from `System.IO.Directory` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public static class Directory
        {
            public static System.IO.DirectoryInfo CreateDirectory(string path) => throw null;
            public static void Delete(string path) => throw null;
            public static void Delete(string path, bool recursive) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateDirectories(string path) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateDirectories(string path, string searchPattern) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateDirectories(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateDirectories(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFileSystemEntries(string path) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFileSystemEntries(string path, string searchPattern) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFileSystemEntries(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFileSystemEntries(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFiles(string path) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFiles(string path, string searchPattern) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFiles(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static System.Collections.Generic.IEnumerable<string> EnumerateFiles(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static bool Exists(string path) => throw null;
            public static System.DateTime GetCreationTime(string path) => throw null;
            public static System.DateTime GetCreationTimeUtc(string path) => throw null;
            public static string GetCurrentDirectory() => throw null;
            public static string[] GetDirectories(string path) => throw null;
            public static string[] GetDirectories(string path, string searchPattern) => throw null;
            public static string[] GetDirectories(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static string[] GetDirectories(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static string GetDirectoryRoot(string path) => throw null;
            public static string[] GetFileSystemEntries(string path) => throw null;
            public static string[] GetFileSystemEntries(string path, string searchPattern) => throw null;
            public static string[] GetFileSystemEntries(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static string[] GetFileSystemEntries(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static string[] GetFiles(string path) => throw null;
            public static string[] GetFiles(string path, string searchPattern) => throw null;
            public static string[] GetFiles(string path, string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public static string[] GetFiles(string path, string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public static System.DateTime GetLastAccessTime(string path) => throw null;
            public static System.DateTime GetLastAccessTimeUtc(string path) => throw null;
            public static System.DateTime GetLastWriteTime(string path) => throw null;
            public static System.DateTime GetLastWriteTimeUtc(string path) => throw null;
            public static string[] GetLogicalDrives() => throw null;
            public static System.IO.DirectoryInfo GetParent(string path) => throw null;
            public static void Move(string sourceDirName, string destDirName) => throw null;
            public static void SetCreationTime(string path, System.DateTime creationTime) => throw null;
            public static void SetCreationTimeUtc(string path, System.DateTime creationTimeUtc) => throw null;
            public static void SetCurrentDirectory(string path) => throw null;
            public static void SetLastAccessTime(string path, System.DateTime lastAccessTime) => throw null;
            public static void SetLastAccessTimeUtc(string path, System.DateTime lastAccessTimeUtc) => throw null;
            public static void SetLastWriteTime(string path, System.DateTime lastWriteTime) => throw null;
            public static void SetLastWriteTimeUtc(string path, System.DateTime lastWriteTimeUtc) => throw null;
        }

        // Generated from `System.IO.DirectoryInfo` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public class DirectoryInfo : System.IO.FileSystemInfo
        {
            public void Create() => throw null;
            public System.IO.DirectoryInfo CreateSubdirectory(string path) => throw null;
            public override void Delete() => throw null;
            public void Delete(bool recursive) => throw null;
            public DirectoryInfo(string path) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.DirectoryInfo> EnumerateDirectories() => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.DirectoryInfo> EnumerateDirectories(string searchPattern) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.DirectoryInfo> EnumerateDirectories(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.DirectoryInfo> EnumerateDirectories(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileSystemInfo> EnumerateFileSystemInfos() => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileSystemInfo> EnumerateFileSystemInfos(string searchPattern) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileSystemInfo> EnumerateFileSystemInfos(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileSystemInfo> EnumerateFileSystemInfos(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileInfo> EnumerateFiles() => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileInfo> EnumerateFiles(string searchPattern) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileInfo> EnumerateFiles(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.Collections.Generic.IEnumerable<System.IO.FileInfo> EnumerateFiles(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public override bool Exists { get => throw null; }
            public System.IO.DirectoryInfo[] GetDirectories() => throw null;
            public System.IO.DirectoryInfo[] GetDirectories(string searchPattern) => throw null;
            public System.IO.DirectoryInfo[] GetDirectories(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.IO.DirectoryInfo[] GetDirectories(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public System.IO.FileSystemInfo[] GetFileSystemInfos() => throw null;
            public System.IO.FileSystemInfo[] GetFileSystemInfos(string searchPattern) => throw null;
            public System.IO.FileSystemInfo[] GetFileSystemInfos(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.IO.FileSystemInfo[] GetFileSystemInfos(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public System.IO.FileInfo[] GetFiles() => throw null;
            public System.IO.FileInfo[] GetFiles(string searchPattern) => throw null;
            public System.IO.FileInfo[] GetFiles(string searchPattern, System.IO.EnumerationOptions enumerationOptions) => throw null;
            public System.IO.FileInfo[] GetFiles(string searchPattern, System.IO.SearchOption searchOption) => throw null;
            public void MoveTo(string destDirName) => throw null;
            public override string Name { get => throw null; }
            public System.IO.DirectoryInfo Parent { get => throw null; }
            public System.IO.DirectoryInfo Root { get => throw null; }
            public override string ToString() => throw null;
        }

        // Generated from `System.IO.EnumerationOptions` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public class EnumerationOptions
        {
            public System.IO.FileAttributes AttributesToSkip { get => throw null; set => throw null; }
            public int BufferSize { get => throw null; set => throw null; }
            public EnumerationOptions() => throw null;
            public bool IgnoreInaccessible { get => throw null; set => throw null; }
            public System.IO.MatchCasing MatchCasing { get => throw null; set => throw null; }
            public System.IO.MatchType MatchType { get => throw null; set => throw null; }
            public bool RecurseSubdirectories { get => throw null; set => throw null; }
            public bool ReturnSpecialDirectories { get => throw null; set => throw null; }
        }

        // Generated from `System.IO.File` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public static class File
        {
            public static void AppendAllLines(string path, System.Collections.Generic.IEnumerable<string> contents) => throw null;
            public static void AppendAllLines(string path, System.Collections.Generic.IEnumerable<string> contents, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task AppendAllLinesAsync(string path, System.Collections.Generic.IEnumerable<string> contents, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task AppendAllLinesAsync(string path, System.Collections.Generic.IEnumerable<string> contents, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static void AppendAllText(string path, string contents) => throw null;
            public static void AppendAllText(string path, string contents, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task AppendAllTextAsync(string path, string contents, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task AppendAllTextAsync(string path, string contents, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.IO.StreamWriter AppendText(string path) => throw null;
            public static void Copy(string sourceFileName, string destFileName) => throw null;
            public static void Copy(string sourceFileName, string destFileName, bool overwrite) => throw null;
            public static System.IO.FileStream Create(string path) => throw null;
            public static System.IO.FileStream Create(string path, int bufferSize) => throw null;
            public static System.IO.FileStream Create(string path, int bufferSize, System.IO.FileOptions options) => throw null;
            public static System.IO.StreamWriter CreateText(string path) => throw null;
            public static void Decrypt(string path) => throw null;
            public static void Delete(string path) => throw null;
            public static void Encrypt(string path) => throw null;
            public static bool Exists(string path) => throw null;
            public static System.IO.FileAttributes GetAttributes(string path) => throw null;
            public static System.DateTime GetCreationTime(string path) => throw null;
            public static System.DateTime GetCreationTimeUtc(string path) => throw null;
            public static System.DateTime GetLastAccessTime(string path) => throw null;
            public static System.DateTime GetLastAccessTimeUtc(string path) => throw null;
            public static System.DateTime GetLastWriteTime(string path) => throw null;
            public static System.DateTime GetLastWriteTimeUtc(string path) => throw null;
            public static void Move(string sourceFileName, string destFileName) => throw null;
            public static void Move(string sourceFileName, string destFileName, bool overwrite) => throw null;
            public static System.IO.FileStream Open(string path, System.IO.FileMode mode) => throw null;
            public static System.IO.FileStream Open(string path, System.IO.FileMode mode, System.IO.FileAccess access) => throw null;
            public static System.IO.FileStream Open(string path, System.IO.FileMode mode, System.IO.FileAccess access, System.IO.FileShare share) => throw null;
            public static System.IO.FileStream OpenRead(string path) => throw null;
            public static System.IO.StreamReader OpenText(string path) => throw null;
            public static System.IO.FileStream OpenWrite(string path) => throw null;
            public static System.Byte[] ReadAllBytes(string path) => throw null;
            public static System.Threading.Tasks.Task<System.Byte[]> ReadAllBytesAsync(string path, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static string[] ReadAllLines(string path) => throw null;
            public static string[] ReadAllLines(string path, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task<string[]> ReadAllLinesAsync(string path, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task<string[]> ReadAllLinesAsync(string path, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static string ReadAllText(string path) => throw null;
            public static string ReadAllText(string path, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task<string> ReadAllTextAsync(string path, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task<string> ReadAllTextAsync(string path, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Collections.Generic.IEnumerable<string> ReadLines(string path) => throw null;
            public static System.Collections.Generic.IEnumerable<string> ReadLines(string path, System.Text.Encoding encoding) => throw null;
            public static void Replace(string sourceFileName, string destinationFileName, string destinationBackupFileName) => throw null;
            public static void Replace(string sourceFileName, string destinationFileName, string destinationBackupFileName, bool ignoreMetadataErrors) => throw null;
            public static void SetAttributes(string path, System.IO.FileAttributes fileAttributes) => throw null;
            public static void SetCreationTime(string path, System.DateTime creationTime) => throw null;
            public static void SetCreationTimeUtc(string path, System.DateTime creationTimeUtc) => throw null;
            public static void SetLastAccessTime(string path, System.DateTime lastAccessTime) => throw null;
            public static void SetLastAccessTimeUtc(string path, System.DateTime lastAccessTimeUtc) => throw null;
            public static void SetLastWriteTime(string path, System.DateTime lastWriteTime) => throw null;
            public static void SetLastWriteTimeUtc(string path, System.DateTime lastWriteTimeUtc) => throw null;
            public static void WriteAllBytes(string path, System.Byte[] bytes) => throw null;
            public static System.Threading.Tasks.Task WriteAllBytesAsync(string path, System.Byte[] bytes, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static void WriteAllLines(string path, System.Collections.Generic.IEnumerable<string> contents) => throw null;
            public static void WriteAllLines(string path, System.Collections.Generic.IEnumerable<string> contents, System.Text.Encoding encoding) => throw null;
            public static void WriteAllLines(string path, string[] contents) => throw null;
            public static void WriteAllLines(string path, string[] contents, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task WriteAllLinesAsync(string path, System.Collections.Generic.IEnumerable<string> contents, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task WriteAllLinesAsync(string path, System.Collections.Generic.IEnumerable<string> contents, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static void WriteAllText(string path, string contents) => throw null;
            public static void WriteAllText(string path, string contents, System.Text.Encoding encoding) => throw null;
            public static System.Threading.Tasks.Task WriteAllTextAsync(string path, string contents, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
            public static System.Threading.Tasks.Task WriteAllTextAsync(string path, string contents, System.Text.Encoding encoding, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken)) => throw null;
        }

        // Generated from `System.IO.FileInfo` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public class FileInfo : System.IO.FileSystemInfo
        {
            public System.IO.StreamWriter AppendText() => throw null;
            public System.IO.FileInfo CopyTo(string destFileName) => throw null;
            public System.IO.FileInfo CopyTo(string destFileName, bool overwrite) => throw null;
            public System.IO.FileStream Create() => throw null;
            public System.IO.StreamWriter CreateText() => throw null;
            public void Decrypt() => throw null;
            public override void Delete() => throw null;
            public System.IO.DirectoryInfo Directory { get => throw null; }
            public string DirectoryName { get => throw null; }
            public void Encrypt() => throw null;
            public override bool Exists { get => throw null; }
            public FileInfo(string fileName) => throw null;
            public bool IsReadOnly { get => throw null; set => throw null; }
            public System.Int64 Length { get => throw null; }
            public void MoveTo(string destFileName) => throw null;
            public void MoveTo(string destFileName, bool overwrite) => throw null;
            public override string Name { get => throw null; }
            public System.IO.FileStream Open(System.IO.FileMode mode) => throw null;
            public System.IO.FileStream Open(System.IO.FileMode mode, System.IO.FileAccess access) => throw null;
            public System.IO.FileStream Open(System.IO.FileMode mode, System.IO.FileAccess access, System.IO.FileShare share) => throw null;
            public System.IO.FileStream OpenRead() => throw null;
            public System.IO.StreamReader OpenText() => throw null;
            public System.IO.FileStream OpenWrite() => throw null;
            public System.IO.FileInfo Replace(string destinationFileName, string destinationBackupFileName) => throw null;
            public System.IO.FileInfo Replace(string destinationFileName, string destinationBackupFileName, bool ignoreMetadataErrors) => throw null;
            public override string ToString() => throw null;
        }

        // Generated from `System.IO.FileSystemInfo` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public abstract class FileSystemInfo : System.MarshalByRefObject, System.Runtime.Serialization.ISerializable
        {
            public System.IO.FileAttributes Attributes { get => throw null; set => throw null; }
            public System.DateTime CreationTime { get => throw null; set => throw null; }
            public System.DateTime CreationTimeUtc { get => throw null; set => throw null; }
            public abstract void Delete();
            public abstract bool Exists { get; }
            public string Extension { get => throw null; }
            protected FileSystemInfo() => throw null;
            protected FileSystemInfo(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.StreamingContext context) => throw null;
            public virtual string FullName { get => throw null; }
            protected string FullPath;
            public virtual void GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.StreamingContext context) => throw null;
            public System.DateTime LastAccessTime { get => throw null; set => throw null; }
            public System.DateTime LastAccessTimeUtc { get => throw null; set => throw null; }
            public System.DateTime LastWriteTime { get => throw null; set => throw null; }
            public System.DateTime LastWriteTimeUtc { get => throw null; set => throw null; }
            public abstract string Name { get; }
            protected string OriginalPath;
            public void Refresh() => throw null;
            public override string ToString() => throw null;
        }

        // Generated from `System.IO.MatchCasing` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public enum MatchCasing
        {
            CaseInsensitive,
            CaseSensitive,
            PlatformDefault,
        }

        // Generated from `System.IO.MatchType` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public enum MatchType
        {
            Simple,
            Win32,
        }

        // Generated from `System.IO.SearchOption` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
        public enum SearchOption
        {
            AllDirectories,
            TopDirectoryOnly,
        }

        namespace Enumeration
        {
            // Generated from `System.IO.Enumeration.FileSystemEntry` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
            public struct FileSystemEntry
            {
                public System.IO.FileAttributes Attributes { get => throw null; }
                public System.DateTimeOffset CreationTimeUtc { get => throw null; }
                public System.ReadOnlySpan<System.Char> Directory { get => throw null; }
                public System.ReadOnlySpan<System.Char> FileName { get => throw null; }
                // Stub generator skipped constructor 
                public bool IsDirectory { get => throw null; }
                public bool IsHidden { get => throw null; }
                public System.DateTimeOffset LastAccessTimeUtc { get => throw null; }
                public System.DateTimeOffset LastWriteTimeUtc { get => throw null; }
                public System.Int64 Length { get => throw null; }
                public System.ReadOnlySpan<System.Char> OriginalRootDirectory { get => throw null; }
                public System.ReadOnlySpan<System.Char> RootDirectory { get => throw null; }
                public System.IO.FileSystemInfo ToFileSystemInfo() => throw null;
                public string ToFullPath() => throw null;
                public string ToSpecifiedFullPath() => throw null;
            }

            // Generated from `System.IO.Enumeration.FileSystemEnumerable<>` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
            public class FileSystemEnumerable<TResult> : System.Collections.Generic.IEnumerable<TResult>, System.Collections.IEnumerable
            {
                // Generated from `System.IO.Enumeration.FileSystemEnumerable<>+FindPredicate` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
                public delegate bool FindPredicate(ref System.IO.Enumeration.FileSystemEntry entry);


                // Generated from `System.IO.Enumeration.FileSystemEnumerable<>+FindTransform` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
                public delegate TResult FindTransform(ref System.IO.Enumeration.FileSystemEntry entry);


                public FileSystemEnumerable(string directory, System.IO.Enumeration.FileSystemEnumerable<TResult>.FindTransform transform, System.IO.EnumerationOptions options = default(System.IO.EnumerationOptions)) => throw null;
                public System.Collections.Generic.IEnumerator<TResult> GetEnumerator() => throw null;
                System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => throw null;
                public System.IO.Enumeration.FileSystemEnumerable<TResult>.FindPredicate ShouldIncludePredicate { get => throw null; set => throw null; }
                public System.IO.Enumeration.FileSystemEnumerable<TResult>.FindPredicate ShouldRecursePredicate { get => throw null; set => throw null; }
            }

            // Generated from `System.IO.Enumeration.FileSystemEnumerator<>` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
            public abstract class FileSystemEnumerator<TResult> : System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.Collections.Generic.IEnumerator<TResult>, System.Collections.IEnumerator, System.IDisposable
            {
                protected virtual bool ContinueOnError(int error) => throw null;
                public TResult Current { get => throw null; }
                object System.Collections.IEnumerator.Current { get => throw null; }
                public void Dispose() => throw null;
                protected virtual void Dispose(bool disposing) => throw null;
                public FileSystemEnumerator(string directory, System.IO.EnumerationOptions options = default(System.IO.EnumerationOptions)) => throw null;
                public bool MoveNext() => throw null;
                protected virtual void OnDirectoryFinished(System.ReadOnlySpan<System.Char> directory) => throw null;
                public void Reset() => throw null;
                protected virtual bool ShouldIncludeEntry(ref System.IO.Enumeration.FileSystemEntry entry) => throw null;
                protected virtual bool ShouldRecurseIntoEntry(ref System.IO.Enumeration.FileSystemEntry entry) => throw null;
                protected abstract TResult TransformEntry(ref System.IO.Enumeration.FileSystemEntry entry);
            }

            // Generated from `System.IO.Enumeration.FileSystemName` in `System.IO.FileSystem, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a`
            public static class FileSystemName
            {
                public static bool MatchesSimpleExpression(System.ReadOnlySpan<System.Char> expression, System.ReadOnlySpan<System.Char> name, bool ignoreCase = default(bool)) => throw null;
                public static bool MatchesWin32Expression(System.ReadOnlySpan<System.Char> expression, System.ReadOnlySpan<System.Char> name, bool ignoreCase = default(bool)) => throw null;
                public static string TranslateWin32Expression(string expression) => throw null;
            }

        }
    }
}
